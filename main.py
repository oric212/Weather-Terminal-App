
import requests


weather_codes = {
    0: "Clear ☀️",
    1: "Mainly Clear 🌤",
    2: "Partly Cloudy ⛅",
    3: "Overcast ☁️",
    45: "Fog 🌫",
    48: "Depositing rime fog ❄️",
    51: "Drizzle 🌦",
    53: "Drizzle 🌦",
    55: "Drizzle 🌦",
    61: "Rain 🌧",
    63: "Rain 🌧",
    65: "Rain 🌧",
    71: "Snow ❄️",
    73: "Snow ❄️",
    75: "Snow ❄️",
    80: "Rain showers 🌧",
    81: "Rain showers 🌧",
    82: "Rain showers 🌧",
    95: "Thunderstorm ⛈",
    99: "Thunderstorm with hail ⛈"
}


def get_current_location():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        if data["status"] == "success":
             return data["city"],data["country"],data["lat"],data["lon"]
        else:
            print("could not get location")
            return None, None, None, None
    except requests.RequestException:
        print("Network error occurred")
        return None, None, None, None



def get_current_weather(lat,lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            current = data["current_weather"]
            return current["temperature"],current["time"],current["weathercode"]
        else:
            print("Failed to get weather data")
            return None, None, None
    except requests.RequestException:
        print("Network error occurred")
        return None, None, None

def format_time(time):
    date_part, time_part = time.split("T")
    date_parts = date_part.split("-")
    formatted_date = "/".join(date_parts[::-1])
    formatted = formatted_date+ " " + time_part
    return formatted


def get_input_from_user():
    user_input = input("Please enter a city name: ").strip()
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={user_input}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                first = data["results"][0]
                city = first["name"]
                country = first["country"]
                latitude = first["latitude"]
                longitude = first["longitude"]
                return city, country, latitude, longitude
            else:
                print("City not found")
                return None, None, None, None
        else:
            print("Failed to get requested data")
            return None, None, None, None
    except requests.RequestException:
        print("Network error occurred")
        return None, None, None, None


def get_requested_weather():
    city, country, latitude, longitude = get_input_from_user()
    if latitude is None or longitude is None:
        print("Cannot get weather for that city.\n")
        return
    requested_temp , requested_time,requested_code = get_current_weather(latitude,longitude)
    print_weather(city,country,requested_time,requested_temp,requested_code)





def print_weather(city,country,time,temp,code):
    adjusted_time = format_time(time)
    weatherindicator = weather_codes.get(code)
    print(f"📍 {city}, {country}")
    print(f"Time: {adjusted_time}")
    print(f"Temp: {temp}°C")
    print(f"Condition: {weatherindicator}")

def handle_requests():
    user_feedback = input("do you want to keep checking the weather? y/n \n")
    while user_feedback == 'y':
        print("\n")
        get_requested_weather()
        user_feedback = input("do you want to keep checking the weather? y/n \n")



city, country, lat, lon = get_current_location()
temp, time, code = get_current_weather(lat,lon)
print_weather(city,country,time,temp,code)
handle_requests()

