import requests
# Notes in 'APIs notes'

# http://api.open-notify.org/iss-now.json; current ISS position

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)
print(response)
print(response.status_code)
response.raise_for_status()

# Getting the actual data; use the .json method
# print(response.json())
data = response.json()
print(data) # the whole thing
print(data['iss_position']) # Just the position of the ISS_POSITION at the current time.
print(data['iss_position']['longitude']) # to get just the longitude of the ISS position
print(data['iss_position']['latitude'])  # to get just the latitude of the ISS position

