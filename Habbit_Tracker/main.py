import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "hanitech"
TOKEN = "2iejopt358t08rh$&R%^&%"
graph_id = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Studying",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

date = datetime.now().strftime("%Y%m%d")
today = datetime(year= 2024, month=5, day=18)
quantity = "120"

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
update_data = {"quantity": "240"} 
response = requests.put(url=update_endpoint, json=update_data, headers=headers)
print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)



