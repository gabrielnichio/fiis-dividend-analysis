# Simulador de investimentos em FIIs

Com esse projeto é possível simular o quanto de renda passiva teria sido possível receber nos dias de hoje se tivessemos investido em um determinado Fundo Imobiliário no passado. 

O projeto leva em consideração um fundo imobiliário específico, data de aplicação inicial, montate da aplicação inicial e aportes mensais (opicional). Os dados utilizados vem do site: https://fiis.com.br/

Os dados retornados são:
- Período disponível: período disponível para simulação com o fundo escolhido.
- Total investido: montante que você investiu do seu próprio bolso.
- Dividendos gerados: total de dividendos gerados no período específicado.
- Quantidade de FIIs comprados.
- Total nos dias de hoje: montante de dinheiro investido de acordo com a quantidade de cotas e sua valorização ao longo do tempo.
- Dividendos projetados por mês: renda passiva projetada para os próximos meses levando em consideração o dividendo da última data de pagamento.

  ![image](https://github.com/user-attachments/assets/8aea9909-bee6-4241-8792-9d84717b537a)

---

Este projeto contém um **backend** em **FastAPI** e um **frontend** em **React**. Siga os passos abaixo para configurar e rodar corretamente.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8+**
- **Node.js (LTS)** e **npm**
- **Git** para clonar o repositório

---

## Rodando o projeto

1. Clone o repositório na sua máquina.
2. Crie um ambiente virtual python.
3. Ative o ambiente virtual e instale as dependências em requirements.txt.
4. Para rodar o backend navegue até a pasta ```backend``` e rode o comando ```fastapi dev api.py```.
5. Para rodar o frontend navegue até a pasta ```frontend/fii-income``` e rode os comandos ```npm install``` e ```npm start```.
