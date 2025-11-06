import requests

LAT = 40.5754#32.817421
LONG =  -122.3836#-85.171463
#
API_KEY = "30cb838fa0840be068201bf5ead34753" 
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
print(API_KEY)
params = {
    "lat": LAT,
    "lon": LONG,
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(OWM_Endpoint, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for item in weather_data["list"]:
    print(item)
    weather_id = item["weather"][0]["id"]
    if int(weather_id) < 700:
        print("Rain")
        will_rain = True
if will_rain:
    print("Bring an Umbrella")

