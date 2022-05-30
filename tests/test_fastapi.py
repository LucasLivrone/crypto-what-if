from src.main import root
import pytest


@pytest.mark.asyncio
async def test_root():
    expected_result = {"message": "Hello World"}
    actual_result = await root()
    assert expected_result == actual_result
