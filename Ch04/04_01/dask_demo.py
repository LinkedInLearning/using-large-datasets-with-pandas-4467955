#%%
import dask.dataframe as ddf

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = ddf.read_parquet(file_name)
df

# %% Maximal tip in percentage where payment is in cash
cash = df[df['payment_type'] == 2]
tip_pct = cash['tip_amount'] / cash['total_amount']
max_tip = tip_pct.max()
max_tip