import requests
from bs4 import BeautifulSoup
from data_creation import createFiiDataFrame

def get_tickers(session, headers):
    tickers = []

    url = f"https://www.clubefii.com.br/fundos_imobiliarios_ranking/2025"

    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    ticker = soup.find_all("a", "nenhuma_cor")

    for i in ticker:
        tickers.append(i.text.strip())
    
    return tickers