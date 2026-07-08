import requests


def get_weather(city):
    API_KEY = "0cad826a84b45dab3343df7cffe57264"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    weather = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
    }

    return weather