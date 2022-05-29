def calculate(
        ars_quantity,
        usd_purchased_price,
        crypto_purchased_price,
        crypto_actual_price,
):
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
