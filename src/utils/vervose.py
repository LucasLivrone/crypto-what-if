def get_verbose_evaluation(calculations, ars_quantity, crypto, date):
    usd_purchased_quantity = calculations["usd_purchased_quantity"]
    crypto_purchased_quantity = calculations["crypto_purchased_quantity"]
    purchased_crypto_actual_value = calculations["purchased_crypto_actual_value"]
    crypto_value_improvement_percentage = calculations["crypto_value_improvement_percentage"]

    verbose_evaluation = f"If you had {ars_quantity} Argentinian pesos in {date} you could have " \
                         f"bought {usd_purchased_quantity} US Dollars and {crypto_purchased_quantity} {crypto} coins." \
                         f"Today that quantity of {crypto} coins have a value of {purchased_crypto_actual_value} US Dollars." \
                         f"The improvement on your {crypto} investment would have been of {crypto_value_improvement_percentage} %"

    calculations["verbose_evaluation"] = verbose_evaluation
    return calculations
