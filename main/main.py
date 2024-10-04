import requests
import pandas as pd

# Getting weather data from the OpenWeather API
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error retrieving data for the city {city}. Error code: {response.status_code}")
        return None

# Displaying and saving data to CSV
def display_weather_data(data):
    if data:
        # Extract important data
        city_name = data['name']
        date = pd.to_datetime(data['dt'], unit='s').strftime('%Y-%m-%d %H:%M:%S')
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display in terminal
        print(f"\nWeather data for {city_name}:")
        print(f"Date: {date}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")

        # Save to CSV
        weather_data = {
            "City": [city_name],
            "Date": [date],
            "Temperature (°C)": [temperature],
            "Humidity (%)": [humidity],
            "Wind Speed (m/s)": [wind_speed]
        }

        df = pd.DataFrame(weather_data)
        df.to_csv(f'weather_data_{city_name}.csv', index=False)
        print(f"\nData saved in 'weather_data_{city_name}.csv'")

# OpenWeather API key
api_key = "Your_API_Key"

# User's city
user_city = input("Enter the city name to get weather data: ")

# Weather data
data = get_weather_data(user_city, api_key)

# Display data and save to CSV
display_weather_data(data)
