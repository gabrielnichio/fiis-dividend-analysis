import { BodyModel } from "../interfaces/request-model";

export async function getDates(ticker: string): Promise<{ start_date: string, end_date: string }> {
    const response = await fetch("http://127.0.0.1:8000/get-dates", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ticker }),
    });
    const data = await response.json();

    return data;
}

export async function getFiiList(): Promise<{ tickers: string[] }> {
    const response = await fetch("http://127.0.0.1:8000/tickers", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });
    const data = await response.json();

    return data;
}

export async function calculateInvestment(body: BodyModel): Promise<any> {
    const response = await fetch("http://127.0.0.1:8000/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
    });
    const data = await response.json();

    return data;
}