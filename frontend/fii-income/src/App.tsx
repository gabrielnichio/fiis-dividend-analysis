import React from 'react';
import './App.css';
import moment from 'moment';

import { useState, useEffect } from "react";
import { Button, Input, Select } from './components/ui';

interface BodyModel{
  ticker: string
  initial_application: number
  application_date: string
  monthly_application: number
}

function App() {
  const [fii, setFii] = useState("");
  const [date, setDate] = useState("");
  const [initialInvestment, setInitialInvestment] = useState(0);
  const [monthlyInvestment, setMonthlyInvestment] = useState(0);
  const [result, setResult] = useState(null);
  const [fiiOptions, setFiiOptions] = useState([]);
  const [startDate, setStartDate] = useState("01/01/2020");
  const [endDate, setEndDate] = useState("");

  useEffect(() => {
    const fetchFiiList = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/tickers", {
          method: "GET",
          headers: { "Content-Type": "application/json" },
        });
        const data = await response.json();
        setFiiOptions(data["tickers"]);
      } catch (error) {
        console.error("Erro trying to fetch FIIs:", error);
      }
    };

    fetchFiiList();
  }, []);

  const fetchInvestmentData = async () => {
    const bodyRequest: BodyModel = {
      ticker: fii,
      initial_application: initialInvestment,
      application_date: date,
      monthly_application: monthlyInvestment,
    };

    const response = await fetch("http://127.0.0.1:8000/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(bodyRequest),
    });
    const data = await response.json();
    setResult(data);
  };

  const getStartEndDates = async (ticker: string) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/get-dates", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticker }),
      });
      const data = await response.json();
      setStartDate(data["start_date"]);
      setEndDate(data["end_date"]);
    } catch (error) {
      console.error("Error trying to get dates:", error);
    }
  };

  return (
    <div className="container">
      <h1 className="title">Simulador de Investimentos em FIIs</h1>
      <div className="input-group">
        <Select value={fii} onChange={(e) => {
          setFii(e.target.value)
          getStartEndDates(e.target.value)
        }}>
          <option value="">Selecione um FII</option>
          {fiiOptions.map((fiiName) => (
            <option key={fiiName} value={fiiName}>
              {fiiName}
            </option>
          ))}
        </Select>
        <Input type="date" value={date} onChange={(e) => setDate(e.target.value)} placeholder="Data" min={startDate} max={endDate}/>
        <Input type="number" value={initialInvestment} onChange={(e) => setInitialInvestment(Number(e.target.value))} placeholder="Aplicação Inicial" />
        <Input type="number" value={monthlyInvestment} onChange={(e) => setMonthlyInvestment(Number(e.target.value))} placeholder="Aplicação Mensal" />
      </div>
      <Button onClick={fetchInvestmentData} className="mt-4">Calcular</Button>

      {startDate && endDate && (
        <div className="date-container">
          <div className="date-box">
            <p>Período disponível: {moment(startDate).format("DD/MM/YYYY")} - {moment(endDate).format("DD/MM/YYYY")}</p>
          </div>
        </div>
      )}

      {result && (
        <div className="result-container">
          <div className="result-box">
            <p>Total Investido: R$ {result["total_invested"]}</p>
          </div>
          <div className="result-box">
            <p>Dividendos Gerados: R$ {result["total_income"]}</p>
          </div>
          <div className="result-box">
            <p>Quantidade de FIIs Comprados: {result["total_num_papers"]}</p>
          </div>
          <div className="result-box">
            <p>Total nos dias de hoje: R$ {result["actual_amount"]}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
