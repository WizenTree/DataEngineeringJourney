# **DAY 6: Real-Time Crypto Data Pipeline (Python + MySQL)**

## **Summary**
Built a working ETL pipline that pulls live crypto data from CoinGecko API, cleans it with Pandas, and stores it in a MySQL database. This simulates a real-world data ingestion use case.

---

## **Tools Used**
- Python (Requests, Pandas)
- MySQL 8.0
- MySQl Connector

---

## **Key Concepts**
- API extraction using `requests`
- Data cleaning and selection with Pandas
- Basic database schema design
- Data loading using MySQL connector

---

## **Pipeline Flow**
1. **Extract**: Pull JSON data from API
2. **Transform**: Select relevant fields, clean and rename
3. **Load**: Create MySQL table and insert rows

---

## **Code Snippet**
```python
#main.py
from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_data_to_mysql

if __name__ == "__main__":
  df = extract_crypto_data()
  df = transform_crypto_data(df)
  load_data_to_mysql(df)
```
