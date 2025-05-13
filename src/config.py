import os

LOGS_FOLDER = "./logs"
DATA_FOLDER = "./data"
SCOPES = [
    'https://mail.google.com/',
    'https://www.googleapis.com/auth/gmail.readonly'
]
CLIENTSECRETS_LOCATION = "./credentials.json"

os.makedirs(LOGS_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)