#%%
import dask.dataframe as ddf

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = ddf.read_parquet(file_name)
df

# %% Percentage of tip in rides where payment was in cash
credit = df[df['payment_type'] == 2]
tip_pct = credit['tip_amount'] / credit['total_amount']
max_tip = tip_pct.max()
