import requests
from datetime import datetime

USERNAME = 'YOURUSERNAME'
TOKEN = 'YOURTOKEN'
GRAPH_ID = 'YOURGRAPHID'


pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#CREATE GRAPH
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Read Graph',
    'unit': 'Pages',
    'type': 'int',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response_2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response_2.text)

#CREATE PIXEL
post_pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

today = datetime.now()

post_pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many pages did you read today? '),
}

response_3 = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response_3.text)



#UPDATE PIXEL
update_pixel_endpoint = f'{post_pixel_endpoint}/20240910'

update_pixel_config = {
    'quantity': '22', 
}

# response_4 = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response_4.text)

#DELETE PIXEL
delete_pixel_endpoint = f'{post_pixel_endpoint}/20240825'

# response_5 = requests.delete(url=delete_pixel_endpoint ,  headers=headers)
# print(response_5.text)