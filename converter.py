import requests
from os import getenv
from fastapi import HTTPException
import aiohttp

APIKEY_ALPHAVANTAGE = getenv('APIKEY_ALPHAVANTAGE')

def sync_converter(from_currency:str, to_currency: str, price:float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={APIKEY_ALPHAVANTAGE}'
    try:
        response= requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400,detail=error)
    data = response.json()

    if not  "Realtime Currency Exchange Rate" in data:
        raise HTTPException(status_code=400,detail="Realtime Currency Exchange Rate not found")
    
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return exchange_rate*price

async def async_converter(from_currency:str, to_currency: str, price:float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={APIKEY_ALPHAVANTAGE}'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()

    except Exception as error:
        raise HTTPException(status_code=400,detail=error)
    
    if not  "Realtime Currency Exchange Rate" in data:
        raise HTTPException(status_code=400,detail="Realtime Currency Exchange Rate not found")
    
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return exchange_rate*price
