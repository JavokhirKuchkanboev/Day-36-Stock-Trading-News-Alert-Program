import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not all([STOCK_API_KEY, NEWS_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID]):
    raise RuntimeError("Missing environment variables")

TELEGRAM_ENDPOINT = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def send_telegram_message(message):
    telegram_parameters = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text":message,
        "parse_mode": "HTML"
    }

    requests.post(url=TELEGRAM_ENDPOINT, data=telegram_parameters)

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}



response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_close = float(yesterday_data["4. close"])
the_day_before_yesturday_data = data_list[1]
the_day_before_yesturday_data_close = float(the_day_before_yesturday_data["4. close"])
difference = yesterday_close - the_day_before_yesturday_data_close
up_down = "🔺" if difference > 0 else "🔻"
percentage_change = (difference / the_day_before_yesturday_data_close) * 100


    
if abs(percentage_change) > 2:

    news_parameters = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    last_three_news = news_data[:3]
    formatted_articles = [
    f"{STOCK_NAME}: {up_down}{abs(percentage_change):.2f}%\n"
    f"Headline: {article['title']}\n"
    f"Brief: {article['description']}"
    for article in last_three_news
]

    for article in formatted_articles:
        send_telegram_message(article)



