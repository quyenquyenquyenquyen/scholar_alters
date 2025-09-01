import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError
from google_auth_httplib2 import AuthorizedHttp
import httplib2
import logging
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional

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
# Configure logging
LOG_DIR = "./logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    force=True,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "gmail_handler.log"), encoding='utf-8'),
        UnicodeStreamHandler()  
    ]
)
logger = logging.getLogger(__name__)


class GmailHandler:
    def __init__(self, data_folder='data', client_secrets_location=None, scopes=None):
        """
        Initialize the GmailHandler class with enhanced CI/CD support.

        Args:
            data_folder (str): Directory to store/read OAuth credentials/tokens.
            client_secrets_location (str): Path to the client secrets JSON file.
            scopes (list): List of scopes for Gmail API access.
        """
        self.data_folder = Path(data_folder)
        self.client_secrets_location = client_secrets_location
        self.scopes = scopes or [
            'https://www.googleapis.com/auth/gmail.readonly'
        ]
        self.use_github_secrets = bool(os.environ.get("USE_GITHUB_SECRETS"))
        self.service = self._get_service()

    def _get_service(self):
        """
        Connect to the Gmail API and return an authorized service instance.
        """
        
        is_github_actions = os.environ.get('GITHUB_ACTIONS') == 'true'
        
        # In GitHub Actions, use environment variables directly
        if self.is_github_actions:
            return self._get_service_github()
        else:
            return self._get_service_local()

    def _get_service_github(self):
        """
        Get Gmail service using environment variables (for GitHub Actions).
        """
        # Get credentials from environment variables
        creds_json = os.environ.get('CREDS_JSON')
        token_json = os.environ.get('TOKEN_CONFIG_JSON')
        
        if not creds_json or not token_json:
            raise ValueError("CREDS_JSON and TOKEN_CONFIG_JSON environment variables are required in GitHub Actions")
        
        try:
            # Parse the token JSON
            token_info = json.loads(token_json)
            creds = Credentials.from_authorized_user_info(token_info, self.scopes)
            
            # Refresh token if needed
            if creds.expired and creds.refresh_token:
                creds.refresh(Request())
            
            # Build and return the Gmail service
            http = AuthorizedHttp(creds, http=httplib2.Http(timeout=30))
            service = build('gmail', 'v1', http=http)
            logger.info("Gmail service created successfully in GitHub Actions.")
            return service
            
        except Exception as e:
            logger.error(f"Failed to create Gmail service in GitHub Actions: {e}")
            raise

    def _get_service_local(self):
        """
        Get Gmail service using local files (for development).
        """
        # Create data folder if it doesn't exist
        self.data_folder.mkdir(parents=True, exist_ok=True)

        token_path = self.data_folder / "token.json"
        credentials_path = self.data_folder / "credentials.json"

        creds = None

        # Load existing token if available
        if token_path.exists():
            try:
                logger.info("Loading credentials from %s", token_path)
                creds = Credentials.from_authorized_user_file(str(token_path), self.scopes)
            except Exception as e:
                logger.warning("Failed to load token.json: %s", e)
                creds = None

        # Refresh or request new credentials if necessary
        if not creds or not creds.valid:
            if creds and creds.expired and getattr(creds, "refresh_token", None):
                try:
                    logger.info("Refreshing expired OAuth credentials.")
                    creds.refresh(Request())
                except RefreshError as e:
                    logger.error("RefreshError while refreshing credentials: %s", e)
                    logger.warning("Attempting interactive flow as a fallback.")
                    creds = self._run_local_flow(credentials_path)
            else:
                logger.info("No valid OAuth credentials found. Starting local interactive OAuth flow.")
                creds = self._run_local_flow(credentials_path)

            # Save the credentials for future use
            if creds and creds.valid:
                try:
                    with token_path.open("w") as token_file:
                        json.dump(json.loads(creds.to_json()), token_file)
                    logger.info("Credentials saved to %s", token_path)
                except Exception as e:
                    logger.warning("Failed to save credentials to %s: %s", token_path, e)

        # Validate credentials
        if not creds or not creds.valid:
            raise ValueError("Failed to obtain valid Gmail credentials. Check logs and your secrets/files.")

        # Build and return the Gmail service with network timeout
        http = AuthorizedHttp(creds, http=httplib2.Http(timeout=30))
        service = build('gmail', 'v1', http=http)
        logger.info("Gmail service created successfully.")
        return service

    def _run_local_flow(self, credentials_path):
        """
        Run interactive local OAuth flow and return credentials.
        
        Args:
            credentials_path (Path): Path to credentials file.
            
        Returns:
            Credentials: OAuth credentials.
        """
        # Determine client secrets file location
        client_secrets_file = None
        if credentials_path.exists():
            client_secrets_file = str(credentials_path)
        elif self.client_secrets_location and Path(self.client_secrets_location).exists():
            client_secrets_file = str(self.client_secrets_location)
        else:
            raise ValueError(
                "Client secrets file not found. Place a credentials.json at the data folder or "
                "provide a valid client_secrets_location."
            )

        logger.info("Starting InstalledAppFlow using client secrets: %s", client_secrets_file)
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, self.scopes)
        creds = flow.run_local_server(port=0, access_type='offline', prompt='consent')
        return creds

    def get_within_day_email_ids(self, user_id: str = 'me', sender_email: str = 'scholaralerts-noreply@google.com'):
        """
        Retrieve email IDs received within the last 2 days from a specified sender with category:updates.

        Args:
            user_id (str): User's email address. Use "me" to indicate the authenticated user.
            sender_email (str): Email address of the sender to filter messages.

        Returns:
            list: List of email IDs received within the last 2 days from the specified sender.
        """
        try:
            # Calculate the timestamp for 48 hours ago
            now = datetime.utcnow()
            two_days_ago = now - timedelta(days=2)
            formatted_two_days_ago = two_days_ago.isoformat() + 'Z'  # 'Z' indicates UTC time
            logger.info("Querying emails since %s", formatted_two_days_ago)

            # Call the Gmail API to fetch the emails with category:updates filter
            results = self.service.users().messages().list(
                userId=user_id,
                q=f'category:updates from:{sender_email} newer_than:2d'
            ).execute()
            logger.debug("Gmail API list result: %s", results)

            messages = results.get('messages', [])
            email_ids = [message['id'] for message in messages]  # Extract email IDs
            logger.info("Found %d email ids: %s", len(email_ids), email_ids)

            return email_ids
        except Exception as error:
            logger.error(f'An error occurred while retrieving emails: {error}')
            return []

    def get_message_from_email_ids(self, email_ids: List[str], user_id: str = 'me'):
        """
        Retrieve a list of message objects from the user's mailbox using the specified email IDs.

        Args:
            user_id (str): User's email address. Use "me" to indicate the authenticated user.
            email_ids (list): List of email IDs to retrieve messages.

        Returns:
            list: List of message objects, each containing the details of the message.
        """
        try:
            messages = []

            # Fetch messages based on the provided email IDs
            for email_id in email_ids:
                message = self.service.users().messages().get(userId=user_id, id=email_id).execute()
                messages.append(message)  # Append the full message object to the list

            return messages

        except Exception as error:
            logger.error(f'An error occurred while listing messages: {error}')
            return []

    def get_message(self, msg_id: str, user_id: str = 'me') -> Optional[Dict]:
        """
        Retrieve the full message using the given message ID.

        Args:
            user_id (str): User's email address. Use "me" to indicate the authenticated user.
            msg_id (str): The ID of the message to retrieve.

        Returns:
            dict: The full message object, or None if an error occurs.
        """
        try:
            message = self.service.users().messages().get(userId=user_id, id=msg_id).execute()
            return message
        except Exception as error:
            logger.error(f'An error occurred while retrieving message {msg_id}: {error}')
            return None


# Example usage
if __name__ == "__main__":
    # Initialize the handler
    handler = GmailHandler(data_folder='data')
    
    # Get email IDs from the last 2 days
    email_ids = handler.get_within_day_email_ids()
    
    # Get full messages
    if email_ids:
        messages = handler.get_message_from_email_ids(email_ids)

        print(f"Retrieved {len(messages)} messages")





