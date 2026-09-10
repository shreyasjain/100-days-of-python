import requests
import datetime
from twilio.rest import Client

STOCK = "SIG"
COMPANY_NAME = "Signet Jewelers Limited "
STOCK_API = "https://www.alphavantage.co/query"
AV_API_KEY = "GVRHR73AV3A4VW92"

NEWS_API = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = "f27e343489c9425aa7259a1c15e1f335"

TWILIO_ACC_SID = "AC0b514da10e363b4fde4aa44004d3b12d"
TWILIO_AUTH_TOKEN = '9714cf0927e5d7a340e4782d207a3405'
FROM_NUMBER = '+14782425170'
TO_NUMBER = '+919649344770'

def get_percentage_change():
    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    stock_parameters = {
        "apikey": AV_API_KEY,
        "symbol": STOCK,
        "function": 'TIME_SERIES_DAILY'
    }

    stock_response = requests.get(STOCK_API, stock_parameters)
    stock_response.raise_for_status()
    stock_data = stock_response.json()

    today = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=2)).date()
    today_price = float(stock_data["Time Series (Daily)"][str(today)]["4. close"])
    yesterday_price = float(stock_data["Time Series (Daily)"][str(yesterday)]["4. close"])

    print(today_price, yesterday_price)
    pc_change = ((today_price - yesterday_price) / yesterday_price) * 100
    return pc_change


def generate_message(percentage):
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_API, news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    article = news_data["articles"][0]
    print(article)

    # Optional: Format the SMS message like this:
    m = f"""
       TSLA: {'🔺' if percentage > 0 else '🔻'}{round(percentage, 2)}%
       Headline: {article["title"][0:50]}
       Brief: {article["description"][0:50]}...
       """
    return m


def send_message(msg):
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
    mid = client.messages.create(
        from_=FROM_NUMBER,
        to=TO_NUMBER,
        body=msg
    )
    print(mid)

# Logic:

percentage_change = get_percentage_change()
print(percentage_change)

if percentage_change <= -5 or percentage_change >= 5:
    message = generate_message(percentage_change)
    send_message(message)
