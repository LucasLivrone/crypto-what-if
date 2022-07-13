import pytest
from src.main import evaluate
from src.utils.crypto_api import get_crypto_actual_price


@pytest.mark.asyncio
async def test_supported_crypto_with_supported_date():
    ars_quantity = 1000
    crypto = "bitcoin"
    date = "30-12-2017"

    crypto_purchased_price = 13620.3618741461
    crypto_actual_price = get_crypto_actual_price(crypto)
    expected_result = {
        "usd_purchased_quantity": 52.96610169491526,
        "crypto_purchased_quantity": 0.0038887440865616398,
        "purchased_crypto_actual_value": 0.0038887440865616398 * crypto_actual_price,
        "crypto_value_improvement_percentage": ((crypto_actual_price * 100) / crypto_purchased_price)-100,
        "verbose_evaluation" : "If you had 1000 Argentinian pesos in 30-12-2017 you could have bought " \
                               "52.96610169491526 US Dollars and 0.0038887440865616398 bitcoin coins." \
                               "Today that quantity of bitcoin coins have a value of " +
                               str(0.0038887440865616398 * crypto_actual_price) + " US Dollars.The improvement on your " \
                               "bitcoin investment would have been of " + str(((crypto_actual_price * 100) / crypto_purchased_price)-100) + " %"

    }

    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result
