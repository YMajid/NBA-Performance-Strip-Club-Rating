import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


def save_as_parquet(json_list, file_name):
    df = pd.DataFrame(json_list)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f'{file_name}.parquet'.format(file_name=file_name))
