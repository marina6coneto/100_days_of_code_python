import requests
from twilio.rest import Client

own_endpoint = '000'
api_key = '000'
account_sid = '000'
auth_token ='000'

MY_LAT = 000
MY_LON = 000

weather_paramns = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(own_endpoint, params=weather_paramns)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = 'It is going to rain today. Remember to bring an umbrella',
        from_ = '000',
        to = '000'
    )
    print(message.status)