#%%
import dask.dataframe as ddf

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = ddf.read_parquet(file_name)
df
# %%
credit = df[df['payment_type'] == 2]
credit['tip_amount'] / credit['total_amount']