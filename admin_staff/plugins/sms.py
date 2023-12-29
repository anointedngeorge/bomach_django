import requests

api = "TLecXOJkRRNKNQZkmeTYnpd3pjuHcRxjruSOhiBlRIArirGcoJFXM8WZhCUooV"

def SMS(to_courier=2348133292427, from_message='sharashell', message=''):
    url = "https://api.ng.termii.com/api/sms/send"
    payload = {
            "to": f"{to_courier}",
            "from": f"{from_message}",
            "sms": f"{message}",
            "type": "plain",
            "channel": "generic",
            "api_key": f"{api}",
                # "media": {
                #     "url": "https://media.example.com/file",
                #     "caption": "your media file"
                # }   
        }
    headers = { 'Content-Type': 'application/json' }
    response = requests.request("POST", url, headers=headers, json=payload)
    return response.json()

