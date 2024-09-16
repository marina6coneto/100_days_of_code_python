import requests
from datetime import datetime
import os

GENDER = 'female'
WEIGHT_KG = 60
HEIGHT_CM = 166
AGE = 26 

# Acessar as variáveis de ambiente definidas no sistema
app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
sheet_endpoint = os.getenv("SHEET_ENDPOINT")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD_API")

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercises = input('Tell me which exercises you did: ')

headers = {
    'x-app-id': app_id,
    'x-app-key': api_key,
}

params = {
    'query': exercises,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()

today_date = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')


for exercise in result['exercises']:
    sheet_input = {
        'workout': {
            'date': today_date,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    
    
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_input,
    auth=(
        username,
        password,
    )
)

print(sheet_response.text)