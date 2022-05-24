from src.utils.crypto_api import get_crypto_historical_price
from datetime import datetime, timedelta


# Coingecko free API support dates from May-2013 until present date


def test_supported_crypto_with_supported_date():
    date = "30-12-2017"
    crypto = "bitcoin"
    price = get_crypto_historical_price(crypto, date)
    assert price == 13620.3618741461


def test_supported_crypto_with_unsupported_past_date():
    date = "01-04-2013"
    crypto = "bitcoin"
    result = get_crypto_historical_price(crypto, date)
    assert result == "Date is not supported"


def test_supported_crypto_with_unsupported_future_date():
    present_date = datetime.now()
    tomorrow_date = present_date + timedelta(1)
    tomorrow_date = tomorrow_date.strftime('%d-%m-%Y')  # tomorrow's date in DD-MM-YYYY format
    crypto = "bitcoin"
    result = get_crypto_historical_price(crypto, tomorrow_date)
    assert result == "Date is not supported"


def test_supported_crypto_with_invalid_date_value():
    date = "qwerty"
    crypto = "bitcoin"
    result = get_crypto_historical_price(crypto, date)
    assert result == "Date is not supported"


def test_unsupported_crypto_with_supported_date():
    date = "30-12-2017"
    crypto = "qwerty"
    result = get_crypto_historical_price(crypto, date)
    assert result == "Crypto is not supported"


def test_unsupported_crypto_with_unsupported_past_date():
    date = "01-04-2013"
    crypto = ""
    result = get_crypto_historical_price(crypto, date)
    assert result == "Crypto is not supported"


def test_unsupported_crypto_with_unsupported_future_date():
    present_date = datetime.now()
    tomorrow_date = present_date + timedelta(1)
    tomorrow_date = tomorrow_date.strftime('%d-%m-%Y')  # tomorrow's date in DD-MM-YYYY format
    crypto = "qwerty"
    result = get_crypto_historical_price(crypto, tomorrow_date)
    assert result == "Crypto is not supported"


def test_unsupported_crypto_with_invalid_date_value():
    date = ""
    crypto = ""
    result = get_crypto_historical_price(crypto, date)
    assert result == "Crypto is not supported"
