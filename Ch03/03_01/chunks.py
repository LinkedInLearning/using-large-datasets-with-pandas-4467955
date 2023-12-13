#%% Calculate the average total amount
import pyarrow.parquet as pq

file_name = '../../data/yellow_tripdata_2021-02.parquet'
total, count = 0, 0
for batch in pq.ParquetFile(file_name).iter_batches(batch_size=10_000):
    total += batch['total_amount'].sum().as_py()
    count += len(batch)

print('average total_amount:', total / count)
