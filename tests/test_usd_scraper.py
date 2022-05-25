from src.utils.usd_scraper import get_usd_historical_price


def test_supported_date():
    date = "30-12-2017"
    price = get_usd_historical_price(date)
    assert price == 18.88
