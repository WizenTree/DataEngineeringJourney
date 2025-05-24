import logging
import traceback

def transform_crypto_data(df):
    try:
        df = df[['name', 'symbol', 'current_price']]
        df = df.dropna()
        logging.info("Data transformation successful.")
        return df
    except Exception as e:
        logging.error("Transformation failed: %s", traceback.format_exc())
        raise