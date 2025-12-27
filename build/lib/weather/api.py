import os

import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"


def fetch_current(city, units="metric"):
    response = requests.get(
        f"{BASE_URL}/weather",
        params={"q": city, "appid": API_KEY, "units": units},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


def fetch_forecast(city, units="metric"):
    response = requests.get(
        f"{BASE_URL}/forecast",
        params={"q": city, "appid": API_KEY, "units": units},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
