import requests
import json

config = json.load(open('./config.json'))

def send(subject, text):
    return requests.post(
        config['email']['server'],
        auth=("api", config['email']['key']),
        data={
            "to": config['email']['to'],
            "from": config['email']['from'],
            "subject": subject,
            "text": text
        }
    )
