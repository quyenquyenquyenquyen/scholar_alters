import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import logging
from .constants import *

# Configure logging to both a file and the console
if not os.path.exists("./logs"):
    os.makedirs("./logs")
logging.basicConfig(
    force=True,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler("./logs/connect_to_gmail.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

def get_service(data_folder='.'):
    """
    Connect to the Gmail API and return an authorized service instance.
    
    Args:
        data_folder (str): Directory to store OAuth tokens.
    
    Returns:
        service: Authorized Gmail API service instance.
    """
    creds = None
    token_filename = os.path.join(data_folder, 'token.json')

    # Load credentials from token.json if available
    if os.path.exists(token_filename):
        creds = Credentials.from_authorized_user_file(token_filename, SCOPES)

    # Refresh or request new credentials if necessary
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENTSECRETS_LOCATION, SCOPES)
            creds = flow.run_local_server()

        # Save the credentials for future use in JSON format
        with open(token_filename, 'w') as token_file:
            json.dump(json.loads(creds.to_json()), token_file)

    # Build and return the Gmail service
    service = build('gmail', 'v1', credentials=creds)
    return service


def list_messages_with_labels(service, user_id, label_ids=[]):
    """
    Retrieve a list of message IDs from the user's mailbox that have the specified labels.

    Args:
        service: Authorized Gmail API service instance.
        user_id (str): User's email address. Use "me" to indicate the authenticated user.
        label_ids (list): List of label IDs to filter messages.

    Returns:
        messages (list): List of message objects, each containing a message ID.
    """
    try:
        messages = []
        response = service.users().messages().list(userId=user_id, labelIds=label_ids).execute()

        if 'messages' in response:
            messages.extend(response['messages'])

        # Paginate through all results
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, labelIds=label_ids, pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages

    except Exception as error:
        logging.error(f'An error occurred while listing messages: {error}')


def get_labels_id(service, user_id, label_names=[]):
    """
    Retrieve the label IDs corresponding to given label names.

    Args:
        service: Authorized Gmail API service instance.
        user_id (str): User's email address. Use "me" to indicate the authenticated user.
        label_names (list): List of label names to search for.

    Returns:
        label_ids (list): List of corresponding label IDs.
    """
    try:
        results = service.users().labels().list(userId=user_id).execute()
        labels = results.get('labels', [])

        # Match labels by name
        label_ids = [label['id'] for name in label_names for label in labels if label['name'] == name]
        return label_ids
    except Exception as error:
        logging.error(f'An error occurred while retrieving labels: {error}')


def get_message(service, user_id, msg_id):
    """
    Retrieve the full message using the given message ID.

    Args:
        service: Authorized Gmail API service instance.
        user_id (str): User's email address. Use "me" to indicate the authenticated user.
        msg_id (str): The ID of the message to retrieve.

    Returns:
        message (dict): The full message object.
    """
    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()
        return message
    except Exception as error:
        logging.error(f'An error occurred while retrieving message {msg_id}: {error}')


if __name__ == '__main__':
    # Connect to the Gmail API
    service = get_service()

    # Get the labels' IDs for 'Papers' and 'UNREAD'
    labels = get_labels_id(service, 'me', ['Papers', 'UNREAD'])

    # List all messages with the specified labels
    messages = list_messages_with_labels(service, "me", labels)
    if messages:
        logging.info(f'Found {len(messages)} messages.')
    else:
        logging.info('No messages found.')
