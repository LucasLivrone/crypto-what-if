import os
import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Crypto What If",
    description="Evaluate Argentinians saving decisions between USD and Crypto"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", default=80))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
