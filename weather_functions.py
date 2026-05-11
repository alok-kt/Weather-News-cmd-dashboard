import requests
import os
from dotenv import load_dotenv

import json
from datetime import datetime
filename = "saved_city.json"

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

if not api_key:
    print("No key found!!")
    exit()


def fetch_weather(city):
    """This function fetches the weather data."""

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print(f"City '{city}' not found! Check spelling!")

        elif response.status_code == 401:
            print("Invalid weather API Key!")

        else:
            print(f"Weather API error: {response.status_code}")
        return None
    
    except requests.exceptions.Timeout:
        print("Weather request timed out!")
        return None
    
    except requests.exceptions.ConnectionError:
        print("No internet connection!")
        return None


def weather_display(city):
    """The main display function which displays the
        data from the other 2 functions in a formatted readable way."""
    
    weather_data = fetch_weather(city)

    if not weather_data:
        print(f"No data to be shown for {city}!")
        return
    
    print("=" * 52)
    print("             ⛅ WEATHER UPDATE ⛅           ")
    print("=" * 52)
    
    print(weather_data['name'])
    print("=" * 52)
    print(f"TEMP 🌡️              {weather_data['main']['temp']:.2f} °C")
    print(f"FEELS LIKE           {weather_data['main']['feels_like']:.2f} °C")
    print(f"HUMIDITY 💧          {weather_data['main']['humidity']}%")
    print(f"WIND SPEED 🌬️        {weather_data['wind']['speed']:.2f} m/s")
    print("=" * 52)


def my_weather(city="thrissur"):
    """Fetches only the weather report of one default city. Appends or records each and every
        report as history in a .json file for future comparison usages."""
    
    data = fetch_weather(city)

    if not data:
        print("No data to be returned!")
        return
    
    current_time = datetime.now().strftime("%d-%m-%y | %I:%M %p")


    print("=" * 52)
    print("                WEATHER REPORT         ")
    print("=" * 52)

    print("YOUR CITY: ", data['name'].upper())
    print("Recorded On: ", current_time)
    print("=" * 52)
    print(f"TEMP 🌡️              {data['main']['temp']:.2f} °C")
    print(f"FEELS LIKE          {data['main']['feels_like']:.2f} °C")
    print(f"HUMIDITY 💧          {data['main']['humidity']}%")
    print(f"WIND SPEED 🌬️        {data['wind']['speed']:.2f} m/s")
    print("=" * 52)

    weather_elements = {
        "recorded_time": current_time,
        "city": data['name'],
        "temp": data['main']['temp'],
        "feels": data['main']['feels_like'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed']
    }

    filepath = os.path.join(os.path.dirname(__file__), filename)

    try:
        with open(filepath, "r") as f:
            history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []
    
    history.append(weather_elements)

    with open(filepath, "w") as f:
        json.dump(history, f, indent=4)
