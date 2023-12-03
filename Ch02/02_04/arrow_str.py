# %% Load Data

import pandas as pd

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = pd.read_parquet(file_name)

# %% Size
mb = 1_000_000
df.memory_usage(deep=True).sum() / mb

# %% Arrow backend
df = pd.read_parquet(file_name, dtype_backend='pyarrow')
df.memory_usage(deep=True).sum() / mb

# %% Convert to names
names = {
    1: 'Creative',
    2: 'VeriFone',
}
df['vendor'] = df['VendorID'].map(names)
df['vendor'].memory_usage(deep=True) / mb

# %% Arrow string
df['vendor'] = df['vendor'].astype('string[pyarrow]')
df['vendor'].memory_usage(deep=True) / mb