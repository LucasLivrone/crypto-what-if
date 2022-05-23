import requests


def get_crypto_historical_price(crypto, date):
    coingecko_api_url = "https://api.coingecko.com/api/v3/coins/" + crypto + "/history?date=" + date
    response = requests.get(coingecko_api_url)
    data = response.json()
    price = data['market_data']['current_price']['usd']
    return price
