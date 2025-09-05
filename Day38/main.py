import requests
from datetime import datetime
import os

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
   "x-app-key": API_KEY
}

parameters = {
    "query": input("Tell me which exercise you did: "),

    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutrition_endpoint,json=parameters,headers=headers)
response.raise_for_status()
result = response.json()

sheety_endpoint = SHEET_ENDPOINT

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
      sheety_endpoint,
      json=sheet_inputs,
      auth=(
          USERNAME,
          PASSWORD,
      )
    )

    bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
    }
    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
