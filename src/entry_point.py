
from googleapiclient.discovery import build
from components.auth import gmail
from components.email import labels

def main():
    credentials = gmail.authentication("./src/config/auth/credentials.json", "./src/config/auth/refresh_token.json")
    service = build('gmail', 'v1', credentials=credentials)
    labels.get_labels(service)

if __name__ == '__main__':
    main()