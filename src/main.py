import os
import uvicorn
from fastapi import FastAPI, Path
from src.utils.calculator import calculate
from src.utils.validation import input_is_valid, input_failure


description = """
**Evaluate Argentinians saving decisions between USD and Crypto 💸**

Due to high inflation rates, Argentinians have historically make the choice of saving their income in stronger currencies.

Although the US dollar has always been the favorite choice, thanks to cryptocurrency there are now more options available.

&nbsp;

Have you ever asked yourself the question **"What if I had Invested in Cryptocurrencies before"**?      

Using this API you will be able to select an amount of *Argentinian pesos*, a *cryptocurrency* and *date* in order to check how much your investment would be worth today.      
In order to give more context, it will also check how many US Dollars you would have been able to save with that amount of pesos at that date.

&nbsp;

Disclaimer:
* Since this tool is using a free API to retrieve historical cryptocurrency data, the oldest date available is 01-05-2013.
* The source this tool is using to get ARS-USD historic values saves monthly data, so the latest date available is the previous month of present date.      
(Example: If today is 26-06-2022, then the latest date available is 30-05-2022)  

&nbsp;
"""


tags_metadata = [
    {
        "name": "Evaluation",
        "description": "Calculate and evaluate investment improvement.",
    }
]


app = FastAPI(
    title="Crypto What If",
    description=description,
    docs_url="/",
    version="latest",
    contact={
        "name": "Github",
        "url": "https://github.com/LucasLivrone/crypto-what-if"
    },
    openapi_tags=tags_metadata,
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,  # Used to hide Schemas at Docs site
        "showExtensions": False
    }
)


@app.get("/ars={ars_quantity}/crypto={crypto}/date={date}", tags=["Evaluation"])
async def evaluate(
        ars_quantity: int = Path(description="Argentinians pesos quantity"),
        crypto: str = Path(description="Cryptocurrency name"),
        date: str = Path(description="Date in the following format: DD-MM-YYYY")):
    if input_is_valid(ars_quantity, crypto, date):
        return calculate(ars_quantity, crypto, date)
    else:
        return input_failure(ars_quantity, crypto, date)


if __name__ == "__main__":  # pragma: no cover
    port = int(os.environ.get("PORT", default=80))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
