
def get_labels(service):
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        print('---------')
        for label in labels:
            print(f"{label['name']} --- {label['id']}")