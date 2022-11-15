import json
with open('/Users/almaz/Documents/data.json') as file:
    text = json.loads(file.read())

import requests

message = "Привет, это Бот! Я есть на Git Hub, а ты?"
phone_number = text['phone_number']

url = text['url']
payload = text['token'] + phone_number + "&body=" + message + "&priority=1&referenceId="
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)

print(response.text)
