import requests
from twilio.rest import Client

API_KEY = "929ab889108f375e71945990dbaba033"
LAT = 32.726601
LONG = 74.857025
# Twillio
account_sid = 'AC0b514da10e363b4fde4aa44004d3b12d'
auth_token = 'a78906b7e2786e0c136f966f3d2001e6'
client = Client(account_sid, auth_token)


def umbrella_weather():
    parameters = {
        'lat': LAT,
        'lon': LONG,
        'appid': API_KEY,
        'cnt': 4
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()
    for item in data['list']:
        for weather in item['weather']:
            if weather["id"] < 700:
                return True
    return False


def send_message(text):
    message = client.messages.create(
        from_='+14782425170',
        to='+919649344770',
        body=text
    )

    print(message.sid)


if umbrella_weather():
    send_message('Take Umbrella with you.')
else:
    send_message('No need to take umbrella.')
