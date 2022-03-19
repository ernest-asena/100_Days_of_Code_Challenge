import requests
from datetime import datetime

MY_LAT = 0.173510
MY_LONG = 34.593290

url = ' https://api.sunrise-sunset.org/json'

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0

}
response = requests.get(url, params=parameters)
response.raise_for_status()
sunrise = response.json()['results']['sunrise'].split("T")[1].split(":")[0]
sunset = response.json()['results']['sunset'].split("T")[1].split(":")[0]
time_now = datetime.now().hour
print(sunrise)
print(sunset)
print(time_now)


