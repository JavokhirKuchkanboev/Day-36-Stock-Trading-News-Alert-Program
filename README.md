# Day 35: Stock Price Alert with Telegram Bot

This Python project monitors a specific stock's price and sends Telegram alerts when the stock price changes significantly. If the change exceeds 2%, the script fetches the latest news about the company and sends the top three headlines to your Telegram bot.

---

## Features

- Fetches daily stock prices from [Alpha Vantage](https://www.alphavantage.co/)
- Calculates the percentage change from the previous day
- Sends Telegram notifications for significant price changes
- Fetches latest news headlines from [NewsAPI](https://newsapi.org/) related to the company
- Sends formatted news messages to Telegram

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
Install dependencies:

pip install requests
Set environment variables:
Create a .env file in the project root (or set system environment variables):

STOCK_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_newsapi_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id


Run the script:

python main.py

