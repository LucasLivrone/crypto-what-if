from src.utils.usd_scraper import get_usd_historical_price
# from src.utils.usd_scraper import get_usd_historical_price


def test_supported_date():  # TODO: Mock API results
    date = "30-12-2017"
    # mocker.patch('src.utils.usd_scraper.scrap_price', return_value="$18,88")
    # mocker.patch.object(get_usd_historical_price, "scrap_price", return_value="$18,88")
    price = get_usd_historical_price(date)
    assert price == 18.88


