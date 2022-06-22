from src.utils.calculator import calculate


def test_unsupported_date():
    ars_quantity = 1000
    crypto = "bitcoin"
    date = ""
    expected_result = "Date is not supported"
    actual_result = calculate(ars_quantity, crypto, date)
    assert expected_result == actual_result


def test_unsupported_crypto():
    ars_quantity = 1000
    crypto = ""
    date = "30-12-2017"
    expected_result = "Crypto is not supported"
    actual_result = calculate(ars_quantity, crypto, date)
    assert expected_result == actual_result
