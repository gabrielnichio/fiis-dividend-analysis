from fastapi import FastAPI
from pydantic import BaseModel

from data_preparation import prepare_data


class Item(BaseModel):
    ticker: str
    initial_application: float
    application_date: str
    monthly_application: float


app = FastAPI()


@app.post("/calculate/")
async def calculate_income(item: Item):
    data = prepare_data(
        item.ticker,
        item.initial_application,
        item.application_date,
        item.monthly_application,
    )

    return {
        "total_income": data["total_income"], 
        "total_invested": data["total_invested"], 
        "rest": data["rest"],
        "intial_application": data["initial_application"],
        "cotacao_starting_date": data["cotacao_starting_date"],
        "division": data["division"]
    }
