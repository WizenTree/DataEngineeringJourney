from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_data_to_mysql
import logging
import traceback

logging.basicConfig(filename="pipeline.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

def main():
    logging.info("Pipeline execution started.")
    try:
        df = extract_crypto_data()
        df = transform_crypto_data(df)
        load_data_to_mysql(df)
        logging.info("Pipeline execution completed successfully.")
    except Exception as e:
        logging.error("Pipeline failed :%s", traceback.format_exc())

if __name__ == "__main__":
    main()