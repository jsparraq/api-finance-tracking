import sys

from googleapiclient.discovery import build

from components.auth import gmail
from components.email import labels

from config import logger


def main():
    credentials = gmail.authentication(
        "./src/config/auth/credentials.json", "./src/config/auth/refresh_token.json"
    )
    service = build("gmail", "v1", credentials=credentials)
    label_id = labels.get_id_label(service)


if __name__ == "__main__":
    verbose = 1
    print(sys.argv)
    if len(sys.argv) > 1:
        verbose = int(sys.argv[1])
    logger.configure_logger(verbose)
    main()
