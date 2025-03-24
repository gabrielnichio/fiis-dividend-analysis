import pandas as pd
import numpy as np


def prepare_data(fii_tracked, initial_application, date, monthly_reinvestment):
    df = pd.read_csv("../data/fii-formated.csv")

    df["data_pagamento"] = pd.to_datetime(df["data_pagamento"])

    print(date)

    application_date = pd.to_datetime(date)

    fii_df = df[
        (df["cotacao"] != 0)
        & (df["data_pagamento"] >= application_date)
        & (df["fundo"] == fii_tracked)
    ]

    starting_date = fii_df.iloc[-1]

    num_cotas = np.floor(initial_application / starting_date["cotacao"])
    division = initial_application / starting_date["cotacao"]

    if isinstance(division, int) or isinstance(division, float) and division.is_integer():
        rest = 0
    else:
        rest = np.round(initial_application - (division * starting_date["cotacao"]), 2)


    rest = (initial_application % starting_date["cotacao"])

    fii_df = fii_df.reindex(index=fii_df.index[::-1]).iloc[1:]

    acc = rest

    total_invested = initial_application
    total_dividends_period = 0
    total_num_papers = 0

    for i in range(len(fii_df)):
        line = fii_df.iloc[i]
        month_income = num_cotas * line["rendimento"]

        total_dividends_period += month_income

        acc = monthly_reinvestment + month_income + acc

        if acc / line["cotacao"] > 0:
            num_papers = np.floor(acc / line["cotacao"])
            total_num_papers += num_papers
            total_invested += num_papers * line["cotacao"]
            num_cotas += num_papers

            acc = np.round(acc % line["cotacao"], 2)
        else:
            acc += month_income
            
    return {
        "total_income": np.round(total_dividends_period, 2),
        "total_invested": np.round(total_invested, 2),
        "total_num_papers": total_num_papers,
    }
