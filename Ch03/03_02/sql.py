# %%
import sqlite3
import pandas as pd

db_file = '../../data/yellow_tripdata_2021-02.db'
query_sql = '''
SELECT VendorID, SUM(total_amount) AS revenue
FROM rides
GROUP BY VendorID
'''

conn = sqlite3.connect(db_file)
df = pd.read_sql(query_sql, conn)
df
