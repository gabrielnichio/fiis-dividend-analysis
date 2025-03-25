from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from data_preparation import prepare_data
from utils import startEndDates, tickers


class Infos(BaseModel):
    ticker: str
    initial_application: float
    application_date: str
    monthly_application: float

class FiiSelected(BaseModel):
    ticker: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite o frontend acessar
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os headers
)


@app.post("/calculate/")
async def calculate_income(front_infos: Infos):
    data = prepare_data(
        front_infos.ticker,
        front_infos.initial_application,
        front_infos.application_date,
        front_infos.monthly_application,
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

@app.post("/get-dates/")
async def get_start_end_dates(filter_infos: FiiSelected):
    data = startEndDates(filter_infos.ticker)

    return {
        "start_date": data["start_date"],
        "end_date": data["end_date"]
    }

