import re
import requests
from datetime import datetime

USERNAME = "XXXX"
TOKEN = "XXXX"
GRAPH_ID = "graph1"

pixela_endopint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    }

# response = requests.post(url=pixela_endopint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endopint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji"
    }

headers = {
    "X-USER-TOKEN": TOKEN
    }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endopint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
    }
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endopint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)