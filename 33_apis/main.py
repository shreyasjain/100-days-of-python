import datetime
import smtplib
import time

import requests

MY_LATIUDE = 22.719568
MY_LONGITUDE = 75.857727


def is_iss_overhead():
    iss_response = requests.get('http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    latitude = float(iss_data["iss_position"]["latitude"])
    longitude = float(iss_data["iss_position"]["longitude"])
    print(abs(MY_LATIUDE - latitude), abs(MY_LONGITUDE - longitude))

    if abs(MY_LATIUDE - latitude) <= 5 and abs(MY_LONGITUDE - longitude) <= 5:
        return True
    return False


def is_night():
    parameters = {
        'lat': MY_LATIUDE,
        'lng': MY_LONGITUDE
    }

    response = requests.get(f'https://api.sunrise-sunset.org/v2', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(response.json()['sunrise'].split('T')[1].split(":")[0])
    sunset = int(response.json()['sunset'].split('T')[1].split(":")[0])
    print(data)
    now = datetime.datetime.now().hour
    if sunrise > now and sunset < now:
        return True
    return False


def run_scan():
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login('13sjain4ur7@gmail.com', 'kdja tdlq xzkv dsvi')
            connection.sendmail('13sjain4ur7@gmail.com', 'shreyasjain4all@gmail.com',
                                'Subject:ISS Above You!\n\nLook into the sky buddy! The ISS is above your head. ')


while True:
    run_scan()
    time.sleep(60)
