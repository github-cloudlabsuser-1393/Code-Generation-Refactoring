# Fetch weather data from OpenWeatherMap API
import requests
from datetime import datetime, timedelta

API_KEY = "6dcc02767422269c88731abe88107ef5"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # Using HTTPS
last_request_time = None

def get_weather(city):
    global last_request_time
    
    # Rate limiting - ensure 10 minutes between requests
    #if last_request_time is not None:
    #    time_since_last_request = datetime.now() - last_request_time
    #    if time_since_last_request < timedelta(minutes=10):
    #        wait_time = timedelta(minutes=10) - time_since_last_request
    #        return {"error": f"Please wait {int(wait_time.total_seconds())} seconds before making another request"}
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        last_request_time = datetime.now()
        
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"]
            }
        elif response.status_code == 429:
            return {"error": "API rate limit exceeded. Please try again in 10 minutes"}
        elif response.status_code == 401:
            return {"error": "Invalid API key"}
        elif response.status_code == 404:
            return {"error": f"City '{city}' not found"}
        else:
            return {"error": f"API Error: {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Connection error: {str(e)}"}

if __name__ == "__main__":
    while True:
        city = input("Enter city name (or 'quit' to exit): ")
        if city.lower() == 'quit':
            break
            
        weather = get_weather(city)
        if "error" in weather:
            print(f"Error: {weather['error']}")
        else:
            print(f"\nWeather in {weather['city']}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Conditions: {weather['description']}\n")