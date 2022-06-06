import os
import uvicorn
from fastapi import FastAPI
from src.utils.calculator import calculate


app = FastAPI(
    title="Crypto What If",
    description="Evaluate Argentinians saving decisions between USD and Crypto"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ars={ars_quantity}/crypto={crypto}/date={date}")
async def evaluate(ars_quantity: int, crypto: str, date: str):
    return calculate(ars_quantity, crypto, date)


if __name__ == "__main__":  # pragma: no cover
    port = int(os.environ.get("PORT", default=80))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
