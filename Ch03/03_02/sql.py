# %%
import duckdb
import pandas as pd

db_file = '../../data/yellow_tripdata_2021-02.ddb'
query_sql = '''
SELECT VendorID, SUM(total_amount)
FROM rides
GROUP BY VendorID
'''

conn = duckdb.connect(db_file)
df = pd.read_sql(query_sql, conn)
df