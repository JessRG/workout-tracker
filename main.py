import os
from dotenv import load_dotenv
import requests
from datetime import datetime

# Read configurations and API keys from .env and inject them into system environment variables
load_dotenv()

APP_ID = os.getenv("APP_ID", "")
API_KEY = os.getenv("API_KEY", "")
GENDER = os.getenv("GENDER", "")
WEIGHT_KG = int(os.getenv("WEIGHT_KG", ""))
HEIGHT_CM = int(os.getenv("HEIGHT_CM", ""))
AGE = int(os.getenv("AGE", ""))
SHEET_ID = os.getenv("SHEET_ID", "")

BASE_URL = "https://app.100daysofpython.dev"
SHEET_URL = "https://api.sheety.co"
EXERCISE_ENDPOINT = f"{BASE_URL}/v1/nutrition/natural/exercise"
SHEET_ENDPOINT = f"{SHEET_URL}/{SHEET_ID}/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "Application/json"
}

exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result.get("exercises"):
    workout_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise.get("name").title(),
            "duration": exercise.get("duration_min"),
            "calories": exercise.get("nf_calories"),
        },
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=workout_inputs)
    print(sheet_response.text)