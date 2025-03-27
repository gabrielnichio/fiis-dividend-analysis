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

    total_num_papers = np.floor(initial_application / starting_date["cotacao"])
    rest = np.round(initial_application-(total_num_papers*starting_date["cotacao"]), 2)

    fii_df = fii_df.reindex(index=fii_df.index[::-1]).iloc[1:]

    acc = rest

    total_invested = initial_application
    total_dividends_period = 0
    

    for i in range(len(fii_df)):
        line = fii_df.iloc[i]
        month_income = total_num_papers * line["rendimento"]

        total_dividends_period += month_income

        acc = monthly_reinvestment + month_income + acc

        if acc / line["cotacao"] >= 0:
            num_papers = np.floor(acc / line["cotacao"])
            total_num_papers += num_papers
            total_invested += monthly_reinvestment
            acc = np.round(acc - (line["cotacao"]*num_papers), 2)
            
    return {
        "total_income": np.round(total_dividends_period, 2),
        "total_invested": np.round(total_invested, 2),
        "total_num_papers": total_num_papers,
        "actual_amount": np.round(((total_num_papers)*fii_df.iloc[-1]["cotacao"]), 2),
        "projected_monthly_income": np.round(total_num_papers*fii_df.iloc[-1]["rendimento"], 2)
    }
