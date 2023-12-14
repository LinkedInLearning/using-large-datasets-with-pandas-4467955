# %%
import pandas as pd

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = pd.read_parquet(file_name)
df['total_amount'].plot.box()

# %%
total_med = df['total_amount'].median()
total_med

# %%
def norm_total(value):
  if value <= 0 or value > 1000:
    return total_med
  return value

# %%
%timeit df['total_amount'].apply(norm_total)

# %%
import numba

@numba.vectorize
def norm_total_numba(value):
  if value <= 0 or value > 1000:
    return total_med
  return value

# %%
%%timeit
values = df['total_amount'].to_numpy()
norm_total_numba(values)