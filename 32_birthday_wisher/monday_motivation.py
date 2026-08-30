import random
import datetime
import smtplib

from dateutil.rrule import weekday


def get_quotes():
    with open("quotes.txt", 'r', encoding='utf-8') as file:
        return file.readlines()


def is_monday():
    date = datetime.datetime.now()
    month = date.weekday()
    if weekday == 1:
        return True
    return False


def send_mail(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login('13sjain4ur7@gmail.com', "kdja tdlq xzkv dsvi")
        connection.sendmail('13sjain4ur7@gmail.com', 'shreyasjain4all@gmail.com',
                            f"Subject:Monday Motivation\n\n{quote}")


quotes = get_quotes()

if is_monday():
    quote = random.choice(quotes).encode('ascii', 'ignore').decode('ascii')
    send_mail(quote)
