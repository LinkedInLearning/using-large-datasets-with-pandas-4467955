"""Daily Passengers

Calculate how many passengers rode each day. Use as little memory as you can.
"""

# %%
import pandas as pd

file_name = '../../data/yellow_tripdata_2021-02.parquet'
columns=['tpep_pickup_datetime', 'passenger_count']
df = pd.read_parquet(file_name, columns=columns)
df.groupby(df['tpep_pickup_datetime'].dt.round('D'))['passenger_count'].sum()
