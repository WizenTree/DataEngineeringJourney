from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_data_to_mysql

def main():
    df = extract_crypto_data()
    df = transform_crypto_data(df)
    load_data_to_mysql(df)
    print("Pipeline executed successfully.")

if __name__ == "__main__":
    main()