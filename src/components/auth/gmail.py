import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from components.auth.constants import gmail_scopes


def authentication(credentials_file: str, refresh_token_file: str) -> dict:
    creds = validate_authentication(refresh_token_file)
    if not creds:
        creds = create_credentials(credentials_file, refresh_token_file)

    return creds


def validate_authentication(refresh_token_file: str) -> dict:
    creds = None
    if os.path.exists(refresh_token_file):
        creds = Credentials.from_authorized_user_file(refresh_token_file, gmail_scopes.READ_ONLY)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            return None
    return creds


def create_credentials(credentials_file: str, refresh_token_file: str) -> dict:
    creds = None
    flow = InstalledAppFlow.from_client_secrets_file(credentials_file, gmail_scopes.READ_ONLY)
    creds = flow.run_local_server(port=0)
    with open(refresh_token_file, "w") as token:
        token.write(creds.to_json())

    return creds
