from src.utils.usd_scraper import get_usd_historical_price
from src.utils.crypto_api import get_crypto_historical_price
from src.utils.crypto_api import get_crypto_actual_price


def calculate(
        ars_quantity,
        crypto,
        date,
):
    crypto_purchased_price = get_crypto_historical_price(crypto, date)
    crypto_actual_price = get_crypto_actual_price(crypto)
    for price in [crypto_purchased_price, crypto_actual_price]:
        if isinstance(price, str):
            return price
    usd_purchased_price = get_usd_historical_price(date)

    usd_purchased_quantity = ars_quantity / usd_purchased_price
    crypto_purchased_quantity = usd_purchased_quantity / crypto_purchased_price
    purchased_crypto_actual_value = crypto_purchased_quantity * crypto_actual_price
    crypto_value_improvement_percentage = ((crypto_actual_price * 100) / crypto_purchased_price)-100

    results = {
        "usd_purchased_quantity": usd_purchased_quantity,
        "crypto_purchased_quantity": crypto_purchased_quantity,
        "purchased_crypto_actual_value": purchased_crypto_actual_value,
        "crypto_value_improvement_percentage": crypto_value_improvement_percentage
    }

    return results
