from src.utils.usd_scraper import get_usd_historical_price
from datetime import datetime, timedelta


def test_supported_date():
    date = "30-12-2017"
    price = get_usd_historical_price(date)
    assert price == 18.88


def test_unsupported_past_date():
    date = "30-12-2012"
    result = get_usd_historical_price(date)
    assert result == "Date is not supported"


def test_unsupported_actual_date():
    present_date = datetime.now()
    present_date = present_date.strftime('%d-%m-%Y')  # tomorrow's date in DD-MM-YYYY format
    result = get_usd_historical_price(present_date)
    assert result == "Date is not supported"


def test_unsupported_future_date():
    present_date = datetime.now()
    tomorrow_date = present_date + timedelta(1)
    tomorrow_date = tomorrow_date.strftime('%d-%m-%Y')  # tomorrow's date in DD-MM-YYYY format
    result = get_usd_historical_price(tomorrow_date)
    assert result == "Date is not supported"


def test_invalid_date():
    date = ""
    result = get_usd_historical_price(date)
    assert result == "Date is not supported"


