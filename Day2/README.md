# **DAY 2: Working with Files - CSV, JSON, Excel**

**Summary**:Understood how CSV, JSON, and Excel differ.Learned how to use Pandas to read/write them.

**Tools**:Pandas

**Key Learning**:
- CSV = tabular, JSON = hierarchical, Excel = multi-sheet.
- ingesting real-world data from disk.

```python
Python

import pandas as pd
df = pd.read_csv("data.csv")
df.to_json("output_json")
```
