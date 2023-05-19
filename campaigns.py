import requests
import json

# adv_savushkin_mytarget

with open('resources/adv_tokens.json') as json_file:
    data = json.load(json_file)
access_token = data['adv_savushkin_mytarget']['access_token']

url = 'https://ads.vk.com/api/v2/campaigns.json'

params = {
}

headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, params=params, headers=headers)

print(response.json())
