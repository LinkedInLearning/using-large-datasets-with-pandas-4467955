# %% Load Data

import pandas as pd

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = pd.read_parquet(file_name)

# %% Measure Memory

mb = 1_000_000
df.memory_usage(deep=True).sum() / mb

# %% File Size
from pathlib import Path

Path(file_name).stat().st_size / mb

# %% Calculate median distance by VendorID

df.groupby('VendorID')['trip_distance'].median()

# %% Load subset of columns

df = pd.read_parquet(file_name, columns=['VendorID', 'trip_distance'])
df.memory_usage(deep=True).sum() / mb

# %% Calculate median distance by VendorID
df.groupby('VendorID')['trip_distance'].median()
