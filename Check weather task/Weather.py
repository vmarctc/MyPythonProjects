import requests

api_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("What is your city ?: ")

params = {
    "q": city,
    "appid": "ca19e211cb04737715915bba02dc5c06",
    "units": "metric"
}

res = requests.get(api_url, params=params)

weather_info = res.json()
template = "Current temp in {} is {} celsius.".format(city, weather_info["main"]["temp"])
print(template)
