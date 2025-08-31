import base64
import json
import logging
import sys
import time
import argparse
from html.parser import HTMLParser
from os import path as ospath, makedirs
try:
    from .constants import *
except ImportError:
    from constants import *
try:
    from GmailHandler import GmailHandler
except ImportError:
    from src.GmailHandler import GmailHandler
from .keywords import FIRST_LEVEL_KEYWORDS, SECOND_LEVEL_KEYWORDS, AUTHORS
class UnicodeStreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            if hasattr(self.stream, 'buffer'):
                self.stream.buffer.write(msg.encode('utf-8'))
                self.stream.buffer.write(self.terminator.encode('utf-8'))
            else:
                self.stream.write(msg + self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)
# Setup logging
if not ospath.exists("./logs"):
    makedirs("./logs")
    
logging.basicConfig(
    force=True,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler("./logs/parse_gmail_message.log", encoding='utf-8'),
        UnicodeStreamHandler()  
    ]
)

class Paper:
    def __init__(self, ref):
        self.title = ''
        self.first_labels = []
        self.second_labels = []
        self.data = ''
        self.link = ''
        self.idx = ''
        self.ref = [ref]
        self.author = []
        
    def __str__(self):
        return (f"Title: {self.title}\nData: {self.data}\nLink: {self.link}\n"
               f"Author: {', '.join(self.author)}\nReferences: {', '.join(self.ref)}\n")
    
    def add_label(self, label: str):
        if label in FIRST_LEVEL_KEYWORDS and label not in self.first_labels:
            self.first_labels.append(label)
        if label in SECOND_LEVEL_KEYWORDS and label not in self.second_labels:
            self.second_labels.append(label)
    
    def _generate_label(self):
        title = self.title.lower()
        for first_label, patterns in FIRST_LEVEL_KEYWORDS.items():
            if any(pattern.lower() in title for pattern in patterns):
                self.add_label(first_label)
        for second_label, patterns in SECOND_LEVEL_KEYWORDS.items():
            if any(pattern.lower() in title for pattern in patterns):
                self.add_label(second_label)
    
    def add_title(self, data: str):
        def clean_title(st):
            if st.startswith('['):
                st = st[st.find(']') + 1:]
            return st.replace('\\xe2\\x80\\x8f', '').strip()
            
        cleaned = clean_title(data)
        if cleaned:
            self.title += cleaned + " "
            self.idx = self.title.strip().upper()
            self._generate_label()
        
    def add_data(self, data: str):
        self.data += data + "\n"
        
    def add_ref(self, ref: str):
        if ref not in self.ref:
            self.ref.append(ref)
            
    def add_author(self, author: str):
        if author not in self.author:
            self.author.append(author)
            
    def from_ref_to_author(self):
        for ref in self.ref:
            for author in AUTHORS:
                if author.lower() in ref.lower():
                    self.add_author(author)
                    break
        
    def to_dict(self):
        return {
            "title": self.title.strip(),
            "first_label": self.first_labels,
            "second_label": self.second_labels,
            "data": self.data.strip(),
            "link": self.link,
            "author": self.author,
            "ref": self.ref
        }

class PapersHTMLParser(HTMLParser):
    def __init__(self, author_ref: str):
        super().__init__()
        self.is_title = False
        self.papers = []
        self.ref = author_ref
        
    def handle_starttag(self, tag: str, attrs: list):
        if tag == 'h3':
            self.papers.append(Paper(self.ref))
            self.is_title = True
        elif tag == 'a' and self.is_title:
            for attr in attrs:
                if attr[0].lower() == 'href':
                    self.papers[-1].link = attr[1]
                    break

    def handle_endtag(self, tag: str):
        if tag == 'h3':
            self.is_title = False

    def handle_data(self, data: str):
        if self.papers:
            if self.is_title:
                self.papers[-1].add_title(data)
            else:
                self.papers[-1].add_data(data)

class PaperAggregator:
    def __init__(self):
        self.paper_list = []
        
    def add(self, paper: Paper):
        idx = self.exists_by_title(paper.title)
        if idx >= 0:
            self.paper_list[idx].add_ref(paper.ref[0])
        elif paper.title.strip():
            paper.from_ref_to_author()
            self.paper_list.append(paper)
            
    def exists_by_title(self, title: str) -> int:
        for i, paper in enumerate(self.paper_list):
            if paper.title == title:
                return i
        return -1

def process_once():
    if not ospath.exists(DATA_FOLDER):
        makedirs(DATA_FOLDER)

    # Use GmailHandler class instead of functions
    handler = GmailHandler(data_folder=DATA_FOLDER)
    email_ids = handler.get_within_day_email_ids()
    messages = handler.get_message_from_email_ids(email_ids)
    
    if not messages:
        logging.info('No messages found')
        return False

    logging.info('Found %d messages', len(messages))
    pa = PaperAggregator()
    email_metadata = []

    for i, msg in enumerate(messages):
        logging.info(f"{i+1}/{len(messages)}")
        
        # Extract headers
        headers = {h['name']: h['value'] for h in msg['payload'].get('headers', [])}
        msg_title = headers.get('Subject', '')
        msg_date = headers.get('Date', '')
        
        if not msg_title:
            logging.warning("No title")
            continue

        # Extract message content
        try:
            body_data = msg['payload']['body']['data']
            msg_str = base64.urlsafe_b64decode(body_data.encode('ASCII'))
        except KeyError:
            logging.warning("No body data")
            continue

        parser = PapersHTMLParser(msg_title)
        parser.feed(msg_str.decode('ascii', errors='ignore'))

        for paper in parser.papers:
            pa.add(paper)

        email_metadata.append({
            "message_id": msg['id'],
            "subject": msg_title,
            "date": msg_date,
            "processed": True
        })

    # Export papers
    with open(ospath.join(DATA_FOLDER, 'papers.jsonl'), 'w') as f:
        for paper in pa.paper_list:
            json.dump(paper.to_dict(), f)
            f.write('\n')

    # Export metadata
    with open(ospath.join(DATA_FOLDER, 'processed_emails.jsonl'), 'w') as f:
        for email_data in email_metadata:
            json.dump(email_data, f)
            f.write('\n')

    logging.info("Export completed")
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse Gmail messages for papers.')
    parser.add_argument('--watch', action='store_true', 
                       help='Run continuously and poll at a fixed interval.')
    parser.add_argument('--interval', type=int, default=900, 
                       help='Polling interval in seconds when running with --watch.')
    args = parser.parse_args()

    if not args.watch:
        process_once()
    else:
        logging.info(f"Starting watch mode with interval={args.interval}s")
        while True:
            try:
                process_once()
            except Exception as error:
                logging.error(f'Unhandled error: {error}')
            time.sleep(max(1, args.interval))