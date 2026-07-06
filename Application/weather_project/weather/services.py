import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("API_KEY")

# Base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather_data(city):
    """
    Fetch weather data for a given city.
    Returns JSON data if successful, otherwise None.
    """

    if not API_KEY:
        print("Error: API_KEY not found in .env file")
        return None

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None