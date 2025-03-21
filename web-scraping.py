import requests
from bs4 import BeautifulSoup
from data_creation import createFiiDataFrame

fiis = ["MCCI11", "BTLG11", "VGIP11", "XPLG11", "XPML11", "MALL11"]



headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

session = requests.Session()

data = []

for fii in fiis:

    url = f"https://fiis.com.br/rendimentos/?ticker={fii}"

    response = session.get(url, headers=headers)


    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    target_div = soup.find("div", {"data-accordion-body": fii})

    

    if target_div:
        linhas = target_div.find_all("div", class_="table__linha")

        count = 0

        for batch in range(int(len(linhas[:-5])/6)):

            l = linhas[count*6:(batch+1)*6]

            columns = {
                "fundo": fii,
                "data_pagamento": l[2].text.strip(),
                "cotacao": l[3].text.strip(),
                "dy": l[4].text.strip(),
                "rendimento": l[5].text.strip()
            }
            
            data.append(columns)
            # data[linhas[6*count+1].text.strip()] = [linha.text.strip() for linha in linhas[count*6:(batch+1)*6]]

            count += 1

        print(data)
    else:
        print(f"Div com data-accordion-body={fii} não encontrada!")

createFiiDataFrame(data)

        

    

