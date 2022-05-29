from src.utils.calculator import calculate


def test_calculator():
    ars_quantity = 1000
    usd_purchased_price = 18.88
    crypto_purchased_price = 13620.3618741461
    crypto_actual_price = 40000

    results = calculate(
        ars_quantity,
        usd_purchased_price,
        crypto_purchased_price,
        crypto_actual_price,
    )

    assert results["usd_purchased_quantity"] == 52.96610169491526
    assert results["crypto_purchased_quantity"] == 0.0038887440865616398
    assert results["purchased_crypto_actual_value"] == 155.5497634624656
    assert results["crypto_value_improvement"] == 293.67795341713503
