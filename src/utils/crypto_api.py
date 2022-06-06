import requests
from src.utils.date_validator import date_is_supported


def get_crypto_historical_price(crypto, date):
    coingecko_api_url = "https://api.coingecko.com/api/v3/coins/" + crypto + "/history?date=" + date
    response = requests.get(coingecko_api_url)
    if response.status_code == 200 and date_is_supported(date):
        data = response.json()
        price = data['market_data']['current_price']['usd']
        return price
    elif response.status_code == 200 and not date_is_supported(date) or response.status_code == 400:
        return "Date is not supported"
    else:
        return "Crypto is not supported"


def get_crypto_actual_price(crypto):
    coingecko_api_url = "https://api.coingecko.com/api/v3/simple/price?ids=" + crypto + "&vs_currencies=usd"
    response = requests.get(coingecko_api_url)
    if response.status_code == 200:
        data = response.json()
        price = data[crypto]['usd']
        return price
    else:
        return "Crypto is not supported"
