import pandas as pd
import requests 
import logging
import json
import mysql.connector
import os

logging.basicConfig(filename='pipeline.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    with open('config.json') as f:
        return json.load(f)
    
def fetch_data(api_url):
    try:
        res = requests.get(api_url)
        res.raise_for_status()
        return res.json()['results']
    except Exception as e:
        logging.error(f"Error fetching API data: {e}")
        return[]
    
def process_data(raw_data):
    df = pd.json_normalize(raw_data)
    df = df[['name.first', 'name.last', 'email', 'location.city']]
    df.columns = ['first_name', 'last_name', 'email', 'city']
    return df

def save_to_csv (df, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    logging.info(f"Saved data to {path}")

def push_to_mysql(df, db_config):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(100), city VARCHAR(100))""")
        for _, row in df.iterrows():
            cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", tuple(row))
        conn.commit()
        conn.close()
        logging.info("Data pushed to MySQL successfully")
    except Exception as e:
        logging.error(f"MySQL Error: {e}")

if __name__ == "__main__":
    config = load_config()
    raw = fetch_data(config['api_url'])
    df = process_data(raw)
    save_to_csv(df, config['csv_path'])
    push_to_mysql(df, config['db'])