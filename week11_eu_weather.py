import requests
import json
import time
from datetime import datetime

eu_capitals = [
    {"city": "Vienna", "country": "Austria", "lat": 48.2082, "lon": 16.3738},
    {"city": "Brussels", "country": "Belgium", "lat": 50.8503, "lon": 4.3517},
    {"city": "Sofia", "country": "Bulgaria", "lat": 42.6977, "lon": 23.3219},
    {"city": "Zagreb", "country": "Croatia", "lat": 45.8150, "lon": 15.9819},
    {"city": "Nicosia", "country": "Cyprus", "lat": 35.1856, "lon": 33.3823},
    {"city": "Prague", "country": "Czechia", "lat": 50.0755, "lon": 14.4378},
    {"city": "Copenhagen", "country": "Denmark", "lat": 55.6761, "lon": 12.5683},
    {"city": "Tallinn", "country": "Estonia", "lat": 59.4370, "lon": 24.7536},
    {"city": "Helsinki", "country": "Finland", "lat": 60.1695, "lon": 24.9354},
    {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
    {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
    {"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
    {"city": "Budapest", "country": "Hungary", "lat": 47.4979, "lon": 19.0402},
    {"city": "Dublin", "country": "Ireland", "lat": 53.3498, "lon": -6.2603},
    {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
    {"city": "Riga", "country": "Latvia", "lat": 56.9496, "lon": 24.1052},
    {"city": "Vilnius", "country": "Lithuania", "lat": 54.6872, "lon": 25.2797},
    {"city": "Luxembourg", "country": "Luxembourg", "lat": 49.6116, "lon": 6.1319},
    {"city": "Valletta", "country": "Malta", "lat": 35.8989, "lon": 14.5146},
    {"city": "Amsterdam", "country": "Netherlands", "lat": 52.3676, "lon": 4.9041},
    {"city": "Warsaw", "country": "Poland", "lat": 52.2297, "lon": 21.0122},
    {"city": "Lisbon", "country": "Portugal", "lat": 38.7223, "lon": -9.1393},
    {"city": "Bucharest", "country": "Romania", "lat": 44.4268, "lon": 26.1025},
    {"city": "Bratislava", "country": "Slovakia", "lat": 48.1486, "lon": 17.1077},
    {"city": "Ljubljana", "country": "Slovenia", "lat": 46.0569, "lon": 14.5058},
    {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
    {"city": "Stockholm", "country": "Sweden", "lat": 59.3293, "lon": 18.0686}
]

def get_weather_code_description(code):
    weather_codes = {
        0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy",
        3: "Overcast", 45: "Foggy", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
        77: "Snow grains", 80: "Slight rain showers",
        81: "Moderate rain showers", 82: "Violent rain showers",
        85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }
    return weather_codes.get(code, "Unknown")

def fetch_weather_data(city_data):
    try:
        base_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": city_data["lat"],
            "longitude": city_data["lon"],
            "current_weather": "true",
            "hourly": "temperature_2m,precipitation_probability,weathercode",
            "timezone": "auto",
            "forecast_days": 1
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        current = data.get("current_weather", {})
        current_weather = {
            "temperature": current.get("temperature"),
            "windspeed": current.get("windspeed"),
            "weathercode": current.get("weathercode"),
            "condition": get_weather_code_description(current.get("weathercode", 0)),
            "time": current.get("time")
        }
        
        hourly = data.get("hourly", {})
        hourly_forecast = []
        times = hourly.get("time", [])
        temps = hourly.get("temperature_2m", [])
        precip_probs = hourly.get("precipitation_probability", [])
        weather_codes = hourly.get("weathercode", [])
        
        for i in range(len(times)):
            hourly_forecast.append({
                "time": times[i],
                "temperature": temps[i] if i < len(temps) else None,
                "precipitation_probability": precip_probs[i] if i < len(precip_probs) else None,
                "weathercode": weather_codes[i] if i < len(weather_codes) else None
            })
        
        return {
            "country": city_data["country"],
            "coordinates": {
                "latitude": city_data["lat"],
                "longitude": city_data["lon"]
            },
            "current_weather": current_weather,
            "hourly_forecast": hourly_forecast
        }
    
    except requests.exceptions.Timeout:
        print(f"Timeout error for {city_data['city']}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network error for {city_data['city']}: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Data parsing error for {city_data['city']}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error for {city_data['city']}: {e}")
        return None

def collect_all_weather_data():
    weather_data = {}
    total = len(eu_capitals)
    
    print(f"Starting weather data collection for {total} EU capitals...")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    for i, capital in enumerate(eu_capitals, 1):
        city_name = capital["city"]
        print(f"[{i}/{total}] Fetching data for {city_name}, {capital['country']}...", end=" ")
        
        city_weather = fetch_weather_data(capital)
        
        if city_weather:
            weather_data[city_name] = city_weather
            print("Success")
        else:
            print("Failed")
        
        if i < total:
            time.sleep(0.75)
    
    print(f"\nCollection complete. Successfully retrieved data for {len(weather_data)}/{total} cities")
    return weather_data

def save_to_json(data, filename="eu_weather_data.json"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Data saved to {filename}")
        print(f"File size: {len(json.dumps(data)) / 1024:.2f} KB")
    except IOError as e:
        print(f"Error saving file: {e}")
    except Exception as e:
        print(f"Unexpected error while saving: {e}")

def display_summary(data):
    if not data:
        print("No data to display")
        return
    
    print("\n" + "="*60)
    print("WEATHER DATA SUMMARY")
    print("="*60)
    
    temps = []
    for city, info in data.items():
        current_temp = info.get("current_weather", {}).get("temperature")
        if current_temp is not None:
            temps.append(current_temp)
    
    if temps:
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        
        print(f"Average Temperature: {avg_temp:.1f}°C")
        print(f"Highest Temperature: {max_temp:.1f}°C")
        print(f"Lowest Temperature: {min_temp:.1f}°C")
    
    print(f"Cities Processed: {len(data)}")
    print("="*60 + "\n")

def main():
    print("="*60)
    print("EU CAPITALS WEATHER DATA COLLECTOR")
    print("="*60 + "\n")
    
    weather_data = collect_all_weather_data()
    
    if weather_data:
        save_to_json(weather_data)
        display_summary(weather_data)
        print("Process completed successfully")
    else:
        print("No data was collected. Please check your internet connection.")

if __name__ == "__main__":
    main()
