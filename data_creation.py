import pandas as pd

fiis = pd.DataFrame(columns=["data_pagamento", "cotacao", "dy", "rendimento"])


def createFiiDataFrame(data):
    df = pd.DataFrame(data)

    df.to_csv("fiis.csv")
    return 