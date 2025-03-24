import pandas as pd
import numpy as np

def tickers():
    df = pd.read_csv("../data/fii-formated.csv")

    tickers = df["fundo"].unique()

    return tickers.tolist()