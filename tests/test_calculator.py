from src.utils.calculator import calculate
from src.utils.crypto_api import get_crypto_actual_price


# TODO: Mock API results

def test_calculator():
    ars_quantity = 1000
    crypto = "bitcoin"
    date = "30-12-2017"

    crypto_purchased_price = 13620.3618741461
    crypto_actual_price = get_crypto_actual_price(crypto)
    expected_result = {
        "usd_purchased_quantity": 52.96610169491526,
        "crypto_purchased_quantity": 0.0038887440865616398,
        "purchased_crypto_actual_value": 0.0038887440865616398 * crypto_actual_price,
        "crypto_value_improvement": (crypto_actual_price * 100) / crypto_purchased_price
    }

    actual_result = calculate(ars_quantity, crypto, date)
    assert expected_result == actual_result
