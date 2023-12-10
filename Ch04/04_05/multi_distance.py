"""
Using polars, find out what is the median distance for rides with more than one passenger.
"""

# %%
import polars as pl

file_name = '../../data/yellow_tripdata_2021-02.parquet'

df = pl.read_parquet(file_name)
df = df.filter(pl.col('passenger_count') > 1)
df.select(pl.median('trip_distance'))
