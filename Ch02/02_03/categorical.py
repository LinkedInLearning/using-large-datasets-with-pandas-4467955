# %% Load Data

import pandas as pd

file_name = '../../data/yellow_tripdata_2021-02.parquet'
df = pd.read_parquet(file_name)

# %% Convert to names
names = {
    1: 'Creative',
    2: 'VeriFone',
}
df['vendor'] = df['VendorID'].map(names)

# %% Measure Memory

mb = 1_000_000
id_size = df['VendorID'].memory_usage(deep=True) / mb
name_size = df['vendor'].memory_usage(deep=True) / mb
print(f'id size: {id_size}, name size: {name_size}')

# %% Convert to categorical
df['vendor'] = df['vendor'].astype('category')
df['vendor'].memory_usage(deep=True) / mb

# %% Categorical
df['vendor'][:10]

# %% Filter
len(df[df['vendor'] == 'VeriFone'])

# %%
