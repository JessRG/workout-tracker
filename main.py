import os
from dotenv import load_dotenv
import requests

# Read configurations and API keys from .env and inject them into system environment variables
load_dotenv()

APP_ID = os.getenv("APP_ID", "")
API_KEY = os.getenv("API_KEY", "")
GENDER = os.getenv("GENDER", "")
WEIGHT_KG = int(os.getenv("WEIGHT_KG", ""))
HEIGHT_CM = int(os.getenv("HEIGHT_CM", ""))
AGE = int(os.getenv("AGE", ""))

BASE_URL = "https://app.100daysofpython.dev"
EXERCISE_ENDPOINT = f"{BASE_URL}/v1/nutrition/natural/exercise"

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
print(response.json())