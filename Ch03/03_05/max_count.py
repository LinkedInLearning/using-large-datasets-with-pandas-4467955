"""
For each VendorID, what is the maximal number of passengers in a ride?
Load at most 10,000 rows to memory.
"""

# %%
import pyarrow.parquet as pq

file_name = '../../data/yellow_tripdata_2021-02.parquet'
counts = {}  # VendorID -> count
columns = ['VendorID', 'passenger_count']
for batch in pq.ParquetFile(file_name).iter_batches(batch_size=10_000, columns=columns):
    for i in range(len(batch)):
        vid = batch['VendorID'][i]
        count = batch['passenger_count'][i].as_py()

        if count is None:
            continue

        count = int(count)
        if count > counts.get(vid, 0):
            counts[vid] = count

for vid, count in counts.items():
    print(f'{vid} -> {count}')
