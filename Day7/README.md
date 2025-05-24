# DAY 7: Production-Ready ETL Pipeline (Logging + Error Handling)

## **Summary**
Improved yesterday's pipeline to handle failures gracefully and track execution using Python logging. Added a config file for secure credentials and made the code modular for reuse.

---

## **Tools Used**
- Python (`logging`, `traceback`)
- MySQL (used from previous setup)

---

## **Key Concepts**
- Centralized logging with `logging.basicConfig()`
- Error handling with `try-except` and stack traces
- Configuration abstraction using `config.py`
- Seperation of concerns in ETL scripts

---

## **Code Snippet**
```python
#main.py
import logging
import traceback
from extract import extract_crypto_data
from transform import transform_crypto_data
from load import load_data_to_mysql

logging.basicConfig(filename="pipeline.log", level=logging.INFO)

try:
  df = extract_crypto_data()
  df = transform_crypto_data(df)
  load_data_to_mysql(df)
except Exception as e:
  logging.error("Pipeline failed: %s", traceback.format_exc())
```
