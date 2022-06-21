import os
import uvicorn
from fastapi import FastAPI
from src.utils.calculator import calculate
from src.utils.validation import input_is_valid, input_failure

app = FastAPI(
    title="Crypto What If",
    description="Evaluate Argentinians saving decisions between USD and Crypto"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ars={ars_quantity}/crypto={crypto}/date={date}")
async def evaluate(ars_quantity: int, crypto: str, date: str):
    if input_is_valid(ars_quantity, crypto, date):
        return calculate(ars_quantity, crypto, date)
    else:
        return input_failure(ars_quantity, crypto)


if __name__ == "__main__":  # pragma: no cover
    port = int(os.environ.get("PORT", default=80))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
