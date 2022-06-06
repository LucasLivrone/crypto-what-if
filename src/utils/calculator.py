from src.utils.usd_scraper import get_usd_historical_price
from src.utils.crypto_api import get_crypto_historical_price
from src.utils.crypto_api import get_crypto_actual_price


def calculate(
        ars_quantity,
        crypto,
        date,
):
    usd_purchased_price = get_usd_historical_price(date)
    crypto_purchased_price = get_crypto_historical_price(crypto, date)
    crypto_actual_price = get_crypto_actual_price(crypto)

    for value in [usd_purchased_price, crypto_purchased_price, crypto_actual_price]:
        if isinstance(value, str):
            return value

    usd_purchased_quantity = ars_quantity / usd_purchased_price
    crypto_purchased_quantity = usd_purchased_quantity / crypto_purchased_price
    purchased_crypto_actual_value = crypto_purchased_quantity * crypto_actual_price
    crypto_value_improvement = (crypto_actual_price * 100) / crypto_purchased_price

    results = {
        "usd_purchased_quantity": usd_purchased_quantity,
        "crypto_purchased_quantity": crypto_purchased_quantity,
        "purchased_crypto_actual_value": purchased_crypto_actual_value,
        "crypto_value_improvement": crypto_value_improvement
    }

    return results
