from .GmailHandler import GmailHandler
from .GmailMessageHandler import PaperAggregator, PapersHTMLParser
import logging
import sys
import codecs

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

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        UnicodeStreamHandler(sys.stdout)  
    ]
)
from .config import DATA_FOLDER
import base64
import os
import json
import shutil
from datetime import datetime, timedelta

def main():
    handler = GmailHandler()
    emails = handler.get_within_day_email_ids()
    messages = handler.get_message_from_email_ids(emails)
    
    if messages:
        logging.info('Found %d messages', len(messages))
    else:
        logging.error('No messages found')
        return

    email_metadata = []
    pa = PaperAggregator()

    for i, msg in enumerate(messages):
        logging.info("Processing message %d/%d", i+1, len(messages))
        msg_content = handler.get_message(msg['id'])
        
        try:
            msg_str = base64.urlsafe_b64decode(msg_content['payload']['body']['data'].encode('ASCII'))
        except KeyError:
            logging.warning("No body data in message")
            continue
        
        # Extract email subject
        msg_title = ''
        for h in msg_content['payload']['headers']:
            if h['name'] == 'Subject':
                msg_title = h['value']
                logging.info("Email subject: %s", msg_title)
                break
                
        if not msg_title:
            logging.warning("No subject found in message")
            continue
        
        # Parse the HTML content of the email
        parser = PapersHTMLParser(msg_title)
        parser.feed(msg_str.decode('ascii', errors='ignore'))
        
        # Add parsed papers to the aggregator
        for paper in parser.papers:
            logging.info("Found paper: %s", paper.title)
            pa.add(paper)
        
        # Store metadata about this processed email
        email_date = ''
        for h in msg_content['payload']['headers']:
            if h['name'] == 'Date':
                email_date = h['value']
                break
                
        email_metadata.append({
            "message_id": msg['id'],
            "subject": msg_title,
            "date": email_date,
            "processed": True
        })

    # Check if papers.jsonl exists and create backup
    papers_jsonl_path = os.path.join(DATA_FOLDER, 'papers.jsonl')
    if os.path.exists(papers_jsonl_path):
        yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        backup_path = os.path.join(DATA_FOLDER, f'{yesterday_date}.jsonl')
        shutil.copy(papers_jsonl_path, backup_path)
        logging.info("Backup created: %s", backup_path)

    # Export papers to JSONL file
    with open(papers_jsonl_path, 'w') as jsonl_file:
        for paper in pa.paper_list:
            json.dump(paper.to_dict(), jsonl_file)
            jsonl_file.write('\n')
    
    # Export email metadata to JSONL file
    emails_jsonl_path = os.path.join(DATA_FOLDER, 'processed_emails.jsonl')
    with open(emails_jsonl_path, 'w') as jsonl_file:
        for email_data in email_metadata:
            json.dump(email_data, jsonl_file)
            jsonl_file.write('\n')
    
    logging.info("Export completed: Papers and email metadata have been written to JSONL files")

if __name__ == '__main__':
    main()