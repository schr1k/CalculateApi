from fastapi import FastAPI, Body
import uvicorn
from models import Tariff
from db import init_db, close_db

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_db()


@app.on_event("shutdown")
async def shutdown_event():
    await close_db()


@app.get("/")
async def test():
    return {"message": "Test"}


@app.post("/rate")
async def upload_tariffs(data=Body()):
    for datet, tariffs in data.items():
        for tariff in tariffs:
            cargo_type = tariff['cargo_type']
            rate = tariff['rate']
            await Tariff.create(cargo_type=cargo_type, rate=rate, date=datet)
    return {"message": "Tariffs uploaded successfully"}


@app.get("/calculate")
async def calculate(cargo_type: str, value: float, order_date: str):
    tariff = await Tariff.filter(cargo_type=cargo_type, date=order_date).first()
    if tariff:
        cost = value * float(tariff.rate)
        return {"cost": cost}
    else:
        return {"message": "Tariff not found for the cargo type"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=80)
