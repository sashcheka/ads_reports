import requests
import datetime as dt
import json


# https://oauth.vk.com/authorize?client_id=51621899&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=offline,stats&response_type=token&v=5.131

def unix_to_date(unix_timestamp):
    datetime = dt.datetime.fromtimestamp(unix_timestamp)
    date_timestamp = datetime.strftime("%Y-%m-%d")
    return date_timestamp


def date_to_unix(date_timestamp):
    datetime = dt.datetime.strptime(date_timestamp, "%Y-%m-%d")
    unix_timestamp = int(datetime.timestamp())
    return unix_timestamp


timestamp_from = '2023-03-01'
timestamp_to = '2023-04-01'
unix_timestamp_from = date_to_unix(timestamp_from)
unix_timestamp_to = date_to_unix(timestamp_to)

app_id = '51621899'
with open('access_token.txt', 'r') as file:
    access_token = file.read().strip()

url = 'https://api.vk.com/method/stats.get'

params = {
    'group_id': 69145727,  # Green
    'access_token': access_token,
    'timestamp_from': unix_timestamp_from,
    'timestamp_to': unix_timestamp_to,
    'interval': 'day',
    'v': '5.131'
}

# response = requests.get(url, params=params).json()
# print(response)


with open('response.json', 'r', encoding='utf-8') as f:
    response = json.load(f)

for item in response['response']:
    print(item['activity'])
    print(f"period_from: {unix_to_date(item['period_from'])}")
    print(f"period_to: {unix_to_date(item['period_to'])}")
    print(f"reach/mobile_reach: {item['reach']['mobile_reach']}")
    print(f"reach/reach: {item['reach']['reach']}")
    print(f"reach/reach_subscribers: {item['reach']['reach_subscribers']}")
    print(f"visitors/mobile_views: {item['visitors']['mobile_views']}")
    print(f"visitors/views: {item['visitors']['views']}")
    print(f"visitors/visitors: {item['visitors']['visitors']}")
    break


# days = len(response['response'])
# print(f'days: {days}')
#
# for i in range(days):
#     try:
#         subscribed = response['response'][i]['activity']['subscribed']
#         print(f'day: {i}, people subscribed: {subscribed}')
#     except Exception:
#         unsubscribed = response['response'][i]['activity']['unsubscribed']
#         print(f'day: {i}, people unsubscribed: {unsubscribed}')
