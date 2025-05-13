import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from .utils import logging
from .config import (
    CLIENTSECRETS_LOCATION,
    SCOPES,
    DATA_FOLDER
)
from datetime import datetime, timedelta

class GmailHandler:
    def __init__(self, data_folder=DATA_FOLDER, client_secrets_location=CLIENTSECRETS_LOCATION, scopes=SCOPES):
        """
        Initialize the GmailHandler class.

        Args:
            data_folder (str): Directory to store OAuth tokens.
            client_secrets_location (str): Path to the client secrets JSON file.
            scopes (list): List of scopes for Gmail API access.
        """
        self.data_folder = data_folder
        self.client_secrets_location = client_secrets_location
        self.scopes = scopes
        self.service = self._get_service()

    def _get_service(self):
        """
        Connect to the Gmail API and return an authorized service instance.

        Returns:
            service: Authorized Gmail API service instance.
        """
        creds = None
        token_filename = os.path.join(self.data_folder, 'token.json')

        # Load credentials from token.json if available
        if os.path.exists(token_filename):
            creds = Credentials.from_authorized_user_file(token_filename, self.scopes)

        # Refresh or request new credentials if necessary
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.client_secrets_location, self.scopes)
                creds = flow.run_local_server()

            # Save the credentials for future use in JSON format
            with open(token_filename, 'w') as token_file:
                json.dump(json.loads(creds.to_json()), token_file)

        # Build and return the Gmail service
        return build('gmail', 'v1', credentials=creds)
    
    def get_within_day_email_ids(self, user_id:str='me', sender_email:str='scholaralerts-noreply@google.com'):
        """
        Retrieve email IDs received within the last day from a specified sender.

        Args:
            user_id (str): User's email address. Use "me" to indicate the authenticated user.
            sender_email (str): Email address of the sender to filter messages.

        Returns:
            email_ids (list): List of email IDs received within the last day from the specified sender.
        """
        try:
            # Calculate the timestamp for 24 hours ago
            now = datetime.utcnow()
            yesterday = now - timedelta(days=1)
            formatted_yesterday = yesterday.isoformat() + 'Z'  # 'Z' indicates UTC time
            logging.info(formatted_yesterday)

            # Call the Gmail API to fetch the emails
            results = self.service.users().messages().list(
                userId=user_id,
                q=f'category:updates from:{sender_email} newer_than:2d'
            ).execute()
            logging.info(results)

            messages = results.get('messages', [])
            email_ids = [message['id'] for message in messages]  # Extract email IDs
            logging.info(email_ids)

            return email_ids
        except Exception as error:
            logging.error(f'An error occurred while retrieving emails: {error}')
            return []

    def get_message_from_email_ids(self, email_ids:list, user_id:str='me'):
        """
        Retrieve a list of message objects from the user's mailbox using the specified email IDs.

        Args:
            user_id (str): User's email address. Use "me" to indicate the authenticated user.
            email_ids (list): List of email IDs to retrieve messages.

        Returns:
            messages (list): List of message objects, each containing the details of the message.
        """
        try:
            messages = []

            # Fetch messages based on the provided email IDs
            for email_id in email_ids:
                message = self.service.users().messages().get(userId=user_id, id=email_id).execute()
                messages.append(message)  # Append the full message object to the list

            return messages

        except Exception as error:
            logging.error(f'An error occurred while listing messages: {error}')
            return []

    def get_message(self, msg_id, user_id:str='me'):
        """
        Retrieve the full message using the given message ID.

        Args:
            user_id (str): User's email address. Use "me" to indicate the authenticated user.
            msg_id (str): The ID of the message to retrieve.

        Returns:
            message (dict): The full message object.
        """
        try:
            message = self.service.users().messages().get(userId=user_id, id=msg_id).execute()
            return message
        except Exception as error:
            logging.error(f'An error occurred while retrieving message {msg_id}: {error}')
            return None
