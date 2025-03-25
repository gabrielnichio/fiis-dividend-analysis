import pandas as pd
import numpy as np

def tickers():
    df = pd.read_csv("../data/fii-formated.csv")

    tickers = df["fundo"].unique()

    return tickers.tolist()

def startEndDates(ticker):
    df = pd.read_csv("../data/fii-formated.csv")

    fii_df = df[
        (df["cotacao"] != 0)
        & (df["fundo"] == ticker)
    ]

    start_date = fii_df.iloc[-1]["data_pagamento"]
    end_date = fii_df.iloc[0]["data_pagamento"]

    return {
        "start_date": start_date,
        "end_date": end_date
    }

