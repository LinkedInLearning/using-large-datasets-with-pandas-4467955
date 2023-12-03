# %% Load Data

import pandas as pd

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = pd.read_parquet(file_name)

# %% Measure Memory

mb = 1_000_000
df.memory_usage(deep=True).sum() / mb

# %% Look at types
df.dtypes

# %% Data range
df['total_amount'].describe()

# %% float32 range
import numpy as np

np.finfo(np.float32)

# %% Smaller Size

amount = df['total_amount'].astype(np.float32)
df['total_amount'].memory_usage(deep=True) / mb

# %% Original Size
amount.memory_usage(deep=True) / mb

# %%
df = pd.read_parquet(file_name, dtype_backend='pyarrow')
df['total_amount'].memory_usage(deep=True) / mb
# %%
df.dtypes