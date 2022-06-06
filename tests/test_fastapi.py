import pytest
from src.main import root
from src.main import evaluate
from src.utils.calculator import calculate


@pytest.mark.asyncio
async def test_root():
    expected_result = {"message": "Hello World"}
    actual_result = await root()
    assert expected_result == actual_result


@pytest.mark.asyncio
async def test_evaluate():
    ars_quantity = 1000
    crypto = "bitcoin"
    date = "30-12-2017"
    expected_result = calculate(ars_quantity, crypto, date)
    actual_result = await evaluate(ars_quantity, crypto, date)
    assert expected_result == actual_result
