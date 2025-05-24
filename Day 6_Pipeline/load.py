import mysql.connector

def load_data_to_mysql(df):
    conn = mysql.connector.connect(host="localhost", user="root", password="py829pjcu", database="demo")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS CRYPTO_DATA (ID VARCHAR(50),SYMBOL VARCHAR(10), NAME VARCHAR(50), CURRENT_PRICE FLOAT, MARKET_CAP BIGINT, TOTAL_VOLUME BIGINT)""")
    for _, row in df.iterrows():
        cursor.execute("INSERT INTO CRYPTO_DATA VALUES (%s,%s,%s,%s,%s,%s)", tuple(row))
    conn.commit()
    cursor.close()
    conn.close()