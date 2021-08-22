
from googleapiclient.discovery import build
from components.auth import gmail

def main():
    credentials = gmail.authentication("./src/config/auth/credentials.json", "./src/config/auth/refresh_token.json")
    service = build('gmail', 'v1', credentials=credentials)

if __name__ == '__main__':
    main()