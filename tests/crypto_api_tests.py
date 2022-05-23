import requests
from src.utils.crypto_api import get_crypto_historical_price


def test_bitcoin_actual_price():
    # Arrange
    crypto = "bitcoin"
    coingecko_api_url = "https://api.coingecko.com/api/v3/simple/price?ids=" + crypto + "&vs_currencies=usd"

    # Act
    response = requests.get(coingecko_api_url)
    data = response.json()
    price = data['bitcoin']['usd']

    # Assert
    assert price >= 0


def test_bitcoin_historical_price():
    # Arrange
    date = "30-12-2017"
    coingecko_api_url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=" + date

    # Act
    response = requests.get(coingecko_api_url)
    data = response.json()
    price = data['market_data']['current_price']['usd']

    # Assert
    assert price == 13620.3618741461


def test_crypto_historical_price():
    # Arrange
    date = "30-12-2017"
    crypto = 'bitcoin'
    coingecko_api_url = "https://api.coingecko.com/api/v3/coins/" + crypto + "/history?date=" + date

    # Act
    response = requests.get(coingecko_api_url)
    data = response.json()
    price = data['market_data']['current_price']['usd']

    # Assert
    assert price == 13620.3618741461


def test_crypto_historical_price_with_function():
    # Arrange
    date = "30-12-2017"
    crypto = 'bitcoin'

    # Act
    price = get_crypto_historical_price(crypto, date)

    # Assert
    assert price == 13620.3618741461
