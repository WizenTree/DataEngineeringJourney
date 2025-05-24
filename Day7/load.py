import mysql.connector
import logging
import traceback
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def load_data_to_mysql(df):
    try:
        conn = mysql.connector.connect(host=DB_HOST,user=DB_USER,password=DB_PASSWORD,database=DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS crypto_prices (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), symbol VARCHAR(50), current_price FLOAT)""")
        for _, row in df.iterrows():
            cursor.execute("INSERT INTO crypto_prices(name, symbol, current_price) VALUES (%s,%s,%s)",(row['name'], row['symbol'], row['current_price']))
        conn.commit()
        conn.close()
        logging.info("Data successfully loaded to MySQL.")

    except Exception as e:
        logging.error("Failed to load data: %s",traceback.format_exc())
        raise