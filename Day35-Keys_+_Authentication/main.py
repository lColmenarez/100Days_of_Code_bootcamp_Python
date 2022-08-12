import requests
from twilio.rest import Client

api_key = ""
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = ""
auth_token = ""


weather_params = {
    "lon": "-99.149375",
    "lat": "19.409199",
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": api_key
}

will_rain = False

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = "It's going to rain today. Remember to bring an ☔",
        from_= "+yyyyyyyyyy",
        to= "+xxxxxxxxxx"
        )
print(message.status)