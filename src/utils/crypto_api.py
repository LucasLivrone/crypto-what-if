import requests


def get_crypto_historical_price(crypto, date):
    coingecko_api_url = "https://api.coingecko.com/api/v3/coins/" + crypto + "/history?date=" + date
    response = requests.get(coingecko_api_url)
    if response.status_code == 200:
        try:
            data = response.json()
            price = data['market_data']['current_price']['usd']
            return price
        except KeyError:
            return "Date is not supported"
    elif response.status_code == 400:
        return "Date is not supported"
    else:
        return "Crypto is not supported"


def get_crypto_actual_price(crypto):
    coingecko_api_url = "https://api.coingecko.com/api/v3/simple/price?ids=" + crypto + "&vs_currencies=usd"
    response = requests.get(coingecko_api_url)
    data = response.json()
    try:
        price = data[crypto]['usd']
        return price
    except KeyError:
        return "Crypto is not supported"
