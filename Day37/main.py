import requests
from datetime import datetime
TOKEN = ""
USERNAME = ""
ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : ID,
    "name" : "Coding Graph",
    "unit" : "Hours",
    "type" : "int",
    "color" : "sora"
}
headers = {
    "X-USER-TOKEN" :TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{ID}"
# today = datetime(day=3, year=2025, month=9)
today = datetime.now()
TODAY = today.strftime("%Y%m%d")
pixel_data = {
    "date" : TODAY,
    "quantity" : input("How many hours did you code?")
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixel_creation_endpoint}/{TODAY}"
update_config = {
    "quantity" : "3"
}

# response = requests.put(url=update_pixel_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_endpoint = update_pixel_endpoint

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)