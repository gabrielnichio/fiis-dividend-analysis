import requests
from bs4 import BeautifulSoup
import time

url = "https://fiis.com.br/rendimentos/?ticker=MCCI11"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

session = requests.Session()
response = session.get(url, headers=headers)


print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

# Encontra a div com data-accordion-body="MCCI11"
target_div = soup.find("div", {"data-accordion-body": "MCCI11"})

data_mcci = {}

if target_div:
    # Encontra todas as divs com class "table__linha" dentro dela
    linhas = target_div.find_all("div", class_="table__linha")

    print(len(linhas[:-5])/6)
    count = 0

    for batch in range(int(len(linhas[:-5])/6)):
        

        data_mcci[linhas[6*count+1].text.strip()] = [linha.text.strip() for linha in linhas[count*6:(batch+1)*6]]

        count += 1

    print(data_mcci)
    
    # for linha in linhas:
    #     if (linha.text.strip() != ""):
    #         data.append(linha.text.strip())

    # print(len(data))

else:
    print("Div com data-accordion-body='MCCI11' não encontrada!")

