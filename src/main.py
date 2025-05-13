from .GmailHandler import GmailHandler
from .GmailMessageHandler import (
    PaperAggregator,
    PapersHTMLParser
)
from .utils import logging
from .config import DATA_FOLDER
import base64
import os
import json
import shutil
from datetime import datetime, timedelta

def main():
    service = GmailHandler()
    emails = service.get_within_day_email_ids()
    messages = service.get_message_from_email_ids(emails)
    if messages:
        logging.info('Found %d messages', len(messages))
    else:
        logging.error('No messages found')
        raise Exception('No messages found')

    email_metadata = []

    pa = PaperAggregator()

    msg_count = 0
    for msg in messages:
        msg_count += 1
        logging.info(f"{msg_count}/{len(messages)}")
        msg_content = service.get_message(msg['id'])
        logging.info(msg_content)
        
        try:
            msg_str = base64.urlsafe_b64decode(msg_content['payload']['body']['data'].encode('ASCII'))
        except KeyError:
            logging.warning("No body data")
            continue  # Skip if email has no body data
        
        # Extract email subject
        msg_title = ''
        for h in msg_content['payload']['headers']:
            if h['name'] == 'Subject':
                msg_title = h['value']
                logging.info(msg_title)
                
        if len(msg_title) == 0:
            logging.warning("No title")
            continue
        
        # Parse the HTML content of the email
        parser = PapersHTMLParser(msg_title)
        parser.feed(str(msg_str))
        
        # Add parsed papers to the aggregator
        for paper in parser.papers:
            logging.info(paper)
            pa.add(paper)
        
        # Store metadata about this processed email
        email_metadata.append({
            "message_id": msg['id'],
            "subject": msg_title,
            "date": next(h['value'] for h in msg_content['payload']['headers'] if h['name'] == 'Date'),
            "processed": True
        })

    # Check if papers.jsonl exists
    papers_jsonl_path = os.path.join(DATA_FOLDER, 'papers.jsonl')
    if os.path.exists(papers_jsonl_path):
        # Create a backup with yesterday's date
        yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        backup_path = os.path.join(DATA_FOLDER, f'{yesterday_date}.jsonl')
        shutil.copy(papers_jsonl_path, backup_path)
        logging.info(f"Backup created: {backup_path}")

    # Export papers to JSONL file
    with open(papers_jsonl_path, 'w', encoding='utf-8') as jsonl_file:
        for paper in pa.paper_list:
            json.dump(paper.to_dict(), jsonl_file)
            jsonl_file.write('\n')
    
    # Export email metadata to JSONL file
    emails_jsonl_path = os.path.join(DATA_FOLDER, 'processed_emails.jsonl')
    with open(emails_jsonl_path, 'w', encoding='utf-8') as jsonl_file:
        for email_data in email_metadata:
            json.dump(email_data, jsonl_file)
            jsonl_file.write('\n')
    
    logging.info("Export completed: Papers and email metadata have been written to JSONL files.")

if __name__ == '__main__':
    main()