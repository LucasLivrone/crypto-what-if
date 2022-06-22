from datetime import datetime, timedelta
from src.main import evaluate
import pytest


@pytest.mark.asyncio
async def test_unsupported_ars_quantity():
    ars_quantity = -1
    crypto = "bitcoin"
    date = "30-12-2017"
    expected_result = ["Argentinian pesos quantity should be greater than 0"]
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_ars_quantity_and_crypto():
    ars_quantity = -1
    crypto = ""
    date = "30-12-2017"
    expected_result = ["Argentinian pesos quantity should be greater than 0",
                       "Crypto is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_ars_quantity_and_date():
    ars_quantity = -1
    crypto = "bitcoin"
    date = ""
    expected_result = ["Argentinian pesos quantity should be greater than 0",
                       "Date is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_ars_quantity_and_crypto_and_date():
    ars_quantity = -1
    crypto = ""
    date = ""
    expected_result = ["Argentinian pesos quantity should be greater than 0",
                       "Crypto is not supported",
                       "Date is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_date():
    ars_quantity = 1000
    crypto = "bitcoin"
    date = ""
    expected_result = ["Date is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_crypto_and_date():
    ars_quantity = 1000
    crypto = ""
    date = ""
    expected_result = ["Crypto is not supported",
                       "Date is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_crypto():
    ars_quantity = 1000
    crypto = ""
    date = "30-12-2017"
    expected_result = ["Crypto is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_past_date():
    ars_quantity = 1000
    crypto = "bitcoin"
    date = "30-12-2012"
    expected_result = ["Date is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_present_date():
    ars_quantity = 1000
    crypto = "bitcoin"
    present_date = datetime.now()
    present_date = present_date.strftime('%d-%m-%Y')  # actual date in DD-MM-YYYY format
    expected_result = ["Date is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, present_date)
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_unsupported_future_date():
    ars_quantity = 1000
    crypto = "bitcoin"
    present_date = datetime.now()
    tomorrow_date = present_date + timedelta(1)
    tomorrow_date = tomorrow_date.strftime('%d-%m-%Y')  # tomorrow's date in DD-MM-YYYY format
    expected_result = ["Date is not supported"]
    actual_result = await evaluate(ars_quantity, crypto, tomorrow_date)
    assert expected_result == actual_result
