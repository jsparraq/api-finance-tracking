from loguru import logger


def get_id_label(service, label_name):
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    if not labels:
        logger.error("No labels found.")
    else:
        for label in labels:
            if label["name"] == label_name:
                return label["id"]
