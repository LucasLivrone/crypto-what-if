import requests
from datetime import datetime


def date_is_supported(date):
    day = int(date[:2])
    month = int(date[3:5])
    year = int(date[-4:])

    present_date = datetime.now()
    input_date = datetime(year, month, day)

    if year < 2013:
        return False
    elif year == 2013 and month < 5:
        return False
    elif input_date > present_date:
        return False
    else:
        return True


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
