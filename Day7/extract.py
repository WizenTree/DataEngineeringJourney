import requests 
import pandas as pd
import logging
import traceback

def extract_crypto_data():
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {"vs_currency": "usd"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        logging.info("Data successfully extracted from API.")
        return df
    except Exception as e:
        logging.error("Failed to extract data: %s", traceback.format_exc())
        raise