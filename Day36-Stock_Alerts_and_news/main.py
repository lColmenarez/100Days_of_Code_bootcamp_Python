import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "XXXX"
NEWS_API_KEY = "XXXX"

TWILIO_SID = "XXXX"
TWILIO_AUTH_TOKEN = "XXX"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
    }

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

diff_percent = round(((float(yesterday_closing_price) - float(day_before_yesterday_closing_price))/float(yesterday_closing_price))*100,1)
print(diff_percent)
up_down = None
if diff_percent > 0:
    up_down = "⬆"
else:
    up_down = "⬇"

if abs(diff_percent) > 0.2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME 
        }
    
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    three_articles = news_response.json()["articles"][:3]
    print(three_articles)
    
    formated_articles = [f"{STOCK}: {up_down}{abs(diff_percent)}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    for article in formated_articles:
        message = client.messages.create(
            body= article,
            from_="+19787363492",
            to="+525566939869"
            )

