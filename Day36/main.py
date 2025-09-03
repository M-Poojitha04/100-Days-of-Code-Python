import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey": ""
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday = data_list[0]
yesterday_closing_stock = yesterday["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_stock = day_before_yesterday["4. close"]

positive_difference = abs(float(yesterday_closing_stock) - float(day_before_yesterday_closing_stock))

percentage_difference = (positive_difference / float(day_before_yesterday_closing_stock)) * 100

print(percentage_difference)

if percentage_difference > 5:
    # print("Get News")
    news_params = {
        "qInTitle" : COMPANY_NAME,
        "apiKey" : ""
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)




