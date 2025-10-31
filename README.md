A simple Python terminal application that shows the current weather and time for your location or any city worldwide. Perfect for learning Python, working with APIs, and creating a user-friendly terminal tool.

Features : 

1.Automatically detects your current location using your IP address.

2.Fetches current weather (temperature and conditions) for your location.

3.Allows you to check weather for any city worldwide.

4.Displays weather conditions with emojis for a nicer visual experience.

5.Shows the current time formatted in DD/MM/YYYY HH:MM style.

6.Simple, interactive terminal interface with option to check multiple cities.


Screenshot:

<img width="656" height="265" alt="Screenshot_4" src="https://github.com/user-attachments/assets/4e21b125-f092-49b7-99ce-6c45a954670a" />


Installation :

Clone this repository: git clone https://github.com/your-username/weather-terminal-app.git

this app requires requests. You can install it with: pip install requests

run the app : python main.py


how to use :
Run the app in your terminal.

Your current location weather will be displayed automatically.

Enter a city name to check weather anywhere in the world.

Repeat as many times as you like by choosing y when prompted.



API used :
IP Geolocation API – http://ip-api.com/json/ → Detects your current location.

Open-Meteo Geocoding API – https://geocoding-api.open-meteo.com/v1/search → Converts city names into latitude/longitude.

Open-Meteo Weather API – https://api.open-meteo.com/v1/forecast → Fetches current weather data.


Weather Codes:

These weather codes are part of the Open-Meteo API and indicate the current weather condition at a location. Each code is mapped to a description and an emoji for easier visualization.

Code	Condition
0	Clear ☀️
1	Mainly Clear 🌤
2	Partly Cloudy ⛅
3	Overcast ☁️
45	Fog 🌫
48	Depositing rime fog ❄️
51-55	Drizzle 🌦
61-65	Rain 🌧
71-75	Snow ❄️
80-82	Rain showers 🌧
95	Thunderstorm ⛈
99	Thunderstorm with hail ⛈

