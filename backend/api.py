from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from data_preparation import prepare_data
from tickers import tickers


class Item(BaseModel):
    ticker: str
    initial_application: float
    application_date: str
    monthly_application: float


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite o frontend acessar
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)


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
        "total_num_papers": data["total_num_papers"],
        "actual_amount": data["actual_amount"]
    }
    
@app.get("/tickers/")
async def get_tickers():
    data = tickers()
    
    return {
        "tickers": data
    }
