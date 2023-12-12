# %% Load Data

import pandas as pd

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = pd.read_parquet(file_name)

# %% Look at types
df.dtypes

# %% Data range
df['total_amount'].describe()

# %% float32 range
import numpy as np

np.finfo(np.float32)

# %% Smaller Size

mb = 1_000_000
df['total_amount'].memory_usage(deep=True) / mb

# %% Original Size

amount = df['total_amount'].astype(np.float32)
amount.memory_usage(deep=True) / mb
# %%
