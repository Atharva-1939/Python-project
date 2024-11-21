import requests
import json

# Your OpenWeatherMap API Key
API_KEY = 'your_api_key'

# Base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    # Construct the URL with the city and API key
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"  # Using metric units for Celsius

    # Send a request to the OpenWeatherMap API
    response = requests.get(url)
    
    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()

        # Parse the necessary details from the response
        city_name = data['name']
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        # Print the weather information
        print(f"Weather in {city_name}:")
        print(f"Description: {weather_desc.capitalize()}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found or API request failed.")

# Get the city from the user and call the function
city = input("Enter city name: ")
get_weather(city)
