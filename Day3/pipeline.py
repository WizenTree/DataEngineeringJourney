import requests
import pandas as pd
import mysql.connector

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

#Check if the response is OK
if response.status_code == 200:
    data = response.json()
    # print(data) #View raw data
else:
    print("Failed to fetch data")

df = pd.DataFrame(data)
# print(df.head())

df.to_csv("users.csv", index=False)

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "py829pjcu",
    database = "demo"
)

cursor = conn.cursor()

#Insert into MySQL
for index, row in df.iterrows():
    cursor.execute("""INSERT INTO users (id, name, email, phone) VALUES (%s, %s, %s, %s)""", (row['id'], row['name'], row['email'], row['phone']))

conn.commit()
conn.close()