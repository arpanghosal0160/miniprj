import requests

WEATHERBIT_API_KEY = "3033e448f8c94ba9be8c6363efcbcedd"
WEATHERAPI_KEY = "69d2dfa4bc0f443c822141130252901"

def get_weather(location):
    weather_info = []

    # Weatherbit API
    try:
        weatherbit_url = f"https://api.weatherbit.io/v2.0/current?city={location}&key={WEATHERBIT_API_KEY}"
        response = requests.get(weatherbit_url)
        data = response.json()

        if "data" in data:
            temp = data["data"][0]["temp"]
            weather_desc = data["data"][0]["weather"]["description"]
            weather_info.append(f"Weatherbit: {weather_desc}, {temp}°C")
        else:
            weather_info.append("Weatherbit API Error.")
    except Exception as e:
        weather_info.append(f"Error fetching Weatherbit data: {e}")

    # WeatherAPI
    try:
        weatherapi_url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={location}"
        response = requests.get(weatherapi_url)
        data = response.json()

        if "current" in data:
            temp = data["current"]["temp_c"]
            weather_desc = data["current"]["condition"]["text"]
            weather_info.append(f"WeatherAPI: {weather_desc}, {temp}°C")
        else:
            weather_info.append(f"WeatherAPI Error: {data.get('error', {}).get('message', 'Unknown error')}")
    except Exception as e:
        weather_info.append(f"Error fetching WeatherAPI data: {e}")

    # Join all responses into a single string and return
    return "\n".join(weather_info)
