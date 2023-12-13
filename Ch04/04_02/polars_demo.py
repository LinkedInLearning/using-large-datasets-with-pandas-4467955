# %%
import polars as pl

file_name = '../../data/yellow_tripdata_2021-02.parquet'

df = pl.read_parquet(file_name)
df.estimated_size(unit='mb')
# %%
import pandas as pd

pd_df = pd.read_parquet(file_name)
pd_df.memory_usage(deep=True).sum() / 1_000_000

# %%
%%timeit
df.group_by('VendorID').agg(
    pl.sum('total_amount')
).sort(
    pl.col('VendorID')
)

# %%
%%timeit
pd_df.groupby('VendorID')['total_amount'].sum().sort_values()
