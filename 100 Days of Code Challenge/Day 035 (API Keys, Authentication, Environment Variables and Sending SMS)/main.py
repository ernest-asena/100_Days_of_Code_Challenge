import requests
from twilio.rest import Client
import config
# import os

account_sid = config.account_sid
auth_token = config.auth_token

client = Client(account_sid, auth_token)
#
API_KEY = config.API_KEY
LONG = 36.726921
LAT = -1.239650
END_POINT = 'https://api.openweathermap.org/data/2.5/onecall'

weather_params = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'units': 'metric',
    'exclude': 'current,minutely,daily'
}

weather_data = requests.get(END_POINT, params=weather_params)
print(weather_data.status_code)
weather = weather_data.json()
weather_slice = weather['hourly'][:12]
# hourly=weather_data.json()['hourly']
# print(hourly[0]['weather'][0]['id'])


def send_msg():
    """Sends a message to my phone number"""
    client.messages.create(
        to=config.MY_PHONE_NO,
        from_=config.MY_TWILIO_PHONE,
        body='GREETINGS.\nIT WILL RAIN TODAY.\nBRING AN UMBRELLA. '

    )


will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print('Bring an Umbrella')
    send_msg()





