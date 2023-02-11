from 
import requests
from datetime import datetime

GENDER = 'male'
WEIGHT_KG = '67.7'
HEIGHT_CM = '173.6'
AGE = '26'

APP_ID = config.NUTRITION_APP_ID
API_KEY = config.NUTRITION_APP_API_KEY

exercise_text = input("Tell me which exercises you did: ")
EXERCISES_END_POINT = ' https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_END_POINT = F'https://api.sheety.co/{config.SHEETY_USERS_API}/myWorkouts/workouts'

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISES_END_POINT, json=parameters, headers=headers)
result = response.json()
print(result)

#
# Duration = response.json()['exercises'][0]['duration_min']
# Calories = response.json()['exercises'][0]['nf_calories']
# Exercise = response.json()['exercises'][0]['name']
# print(Calories)
# print(Duration)
# print(Exercise)
# print(len(response.json()['exercises']))

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

    # sheet_response = requests.post(SHEETY_END_POINT, json=sheet_inputs)     # No Authorization
    # Basic Authorization
    sheet_response = requests.post(
        SHEETY_END_POINT,
        json=sheet_inputs,
        auth=(
            config.SHEETY_USER_NAME,
            config.SHEETY_PASSWORD,
        )
    )

    print(sheet_response.text)


#Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint,
#   json=sheet_inputs,
#   auth=(
#       YOUR USERNAME,
#       YOUR PASSWORD,
#   )
# )
#
# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )