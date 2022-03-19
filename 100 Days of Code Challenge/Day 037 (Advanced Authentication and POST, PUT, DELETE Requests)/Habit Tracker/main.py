import requests
import datetime

import config

TODAY = datetime.date.today().strftime("%Y%m%d")
# YESTERDAY = datetime.date(year=2021, month=11, day=1).strftime("%Y%m%d")

USERNAME = 'ernest'

# Create User
pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = config.pixela_token
params = {
    'token': config.pixela_token,
    'username': 'ernest',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

# Create Graph
graph_endpoint = F"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': 'graph1',
    'name': 'working out',
    'unit': 'minutes',
    'type': 'int',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN,

}
# graph_set = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_set.text)


# Adding a Pixel to the Habit tracker
add_pixel_endpoint = F'{pixela_endpoint}/{USERNAME}/graphs/graph1'
data_to_add = {
    'date': TODAY,
    'quantity': '32',

}

send_pixel = requests.post(url=add_pixel_endpoint, json=data_to_add, headers=headers)
print(send_pixel.text)

# PUT REQUEST
# put_endpoint = F'{pixela_endpoint}/{USERNAME}/graphs/graph1/{YESTERDAY}'
# update_pixel = requests.put(url=put_endpoint, json=data_to_add, headers=headers)
# print(update_pixel.text)

# DELETE REQUEST
# delete_end_point = put_endpoint = F'{pixela_endpoint}/{USERNAME}/graphs/graph1/{YESTERDAY}'
# delete_pixel = requests.delete(url=delete_end_point, headers=headers)
# print(delete_pixel.text)