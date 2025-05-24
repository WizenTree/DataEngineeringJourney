# **DAY 3: Mini Pipeline - API to CSV to MySQL**

**Summary**:Fetched data from API, cleaned with Pandas, stored in CSV, and inserted into MySQL.

**Tools**: Python, Pandas, Requests, MySQL

**Key Learning**:
- Requests + Pandas = gold.
- Push cleaned data into relational DBs.

```python
Python

import requests
data = requests.get("https://api.example.com").json()
df = pd.DataFrame(data)
df.to_csv("output.csv")
```
