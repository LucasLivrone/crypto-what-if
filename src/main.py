import argparse
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
    port = os.getenv('PORT', default=80)  # Open port for deployment to Heroku.

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0", type=str)
    parser.add_argument("--port", default=port, type=int)
    parser.add_argument(
        "--precache-models",
        action="store_true",
        help="Pre-cache all models in memory upon initialization,otherwise dynamically caches models",
    )
    opt = parser.parse_args()
    # if opt.precache_models:
    #     model_dict = precache_models()
    # make the app string equal to whatever the name of this file is

    app_str = ("main:app")

    uvicorn.run(app_str, host=opt.host, port=opt.port, reload=True)
