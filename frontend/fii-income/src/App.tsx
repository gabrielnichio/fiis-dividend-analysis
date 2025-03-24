import React from 'react';
import './App.css';

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

  useEffect(() => {
    const fetchFiiList = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/tickers", {
          method: "GET",
          headers: { "Content-Type": "application/json" }
        }); 
        const data = await response.json();
        setFiiOptions(data["tickers"]);
      } catch (error) {
        console.error("Erro ao buscar FIIs:", error);
      }
    };

    fetchFiiList();
  }, []);

  const fetchInvestmentData = async () => {
    const bodyRequest: BodyModel = {
      ticker: fii,
      initial_application: initialInvestment,
      application_date: date,
      monthly_application: monthlyInvestment
    } 

    const response = await fetch("http://127.0.0.1:8000/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(bodyRequest),
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="p-6 max-w-lg mx-auto">
      <h1 className="text-xl font-bold mb-4">Simulador de Investimentos em FIIs</h1>
      <Select value={fii} onChange={(e) => setFii(e.target.value)}>
        <option value="">Selecione um FII</option>
        {fiiOptions.map((fiiName) => (
          <option key={fiiName} value={fiiName}>
            {fiiName}
          </option>
        ))}
      </Select>
      <Input type="date" value={date} onChange={(e) => setDate(e.target.value)} placeholder="Data" />
      <Input type="number" value={initialInvestment} onChange={(e) => setInitialInvestment(Number(e.target.value))} placeholder="Aplicação Inicial" />
      <Input type="number" value={monthlyInvestment} onChange={(e) => setMonthlyInvestment(Number(e.target.value))} placeholder="Aplicação Mensal" />
      <Button onClick={fetchInvestmentData} className="mt-4">Calcular</Button>
      {result && (
        <div className="mt-6 p-4 border rounded bg-gray-100">
          <p>Total Investido: R$ {result["total_invested"]}</p>
          <p>Dividendos Gerados: R$ {result["total_income"]}</p>
          <p>Quantidade de FIIs Comprados: {result["total_num_papers"]}</p>
        </div>
      )}
    </div>
  );
}

export default App;
