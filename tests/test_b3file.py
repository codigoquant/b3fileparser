import os
import pandas as pd
import polars as pl

from pandas.testing import assert_frame_equal as pandas_assert
from polars.testing import assert_frame_equal as polars_assert
from b3fileparser.b3parser import B3Parser


parser_pandas = B3Parser.create_parser('pandas')
parser_polars = B3Parser.create_parser('polars')



def get_path(name):
    return os.path.join(os.path.dirname(__file__), "sample_data", name)

def generate_test_files():
    for engine in ['polars', 'pandas']:
        parser = B3Parser.create_parser(engine)
        files = ["COTAHIST_A2024.ZIP", "COTAHIST_A2023_test.TXT"]
        for f in files:
            df = parser.read_b3_file(file_path=f'tests/sample_data/{f}')
            if engine == 'polars':
                df.write_parquet(f'tests/sample_data/{engine}_{f}.parquet')
            elif engine == 'pandas':
                df.to_parquet(f'tests/sample_data/{engine}_{f}.parquet')

def test_txt_file_pandas():
    b3_data = parser_pandas.read_b3_file(get_path('COTAHIST_A2023_test.TXT'))
    df_sample = pd.read_parquet("tests/sample_data/pandas_COTAHIST_A2023_test.TXT.parquet")
    pandas_assert(b3_data, df_sample)

def test_zip_file_pandas():
    b3_data =  parser_pandas.read_b3_file(get_path('COTAHIST_A2024.ZIP'))  
    df_sample = pd.read_parquet("tests/sample_data/pandas_COTAHIST_A2024.ZIP.parquet")
    pandas_assert(b3_data, df_sample)

def test_txt_file_polars():
    b3_data = parser_polars.read_b3_file(get_path('COTAHIST_A2023_test.TXT'))
    df_sample = pl.read_parquet("tests/sample_data/polars_COTAHIST_A2023_test.TXT.parquet")
    polars_assert(b3_data, df_sample)

def test_zip_file_polars():
    b3_data =  parser_polars.read_b3_file(get_path('COTAHIST_A2024.ZIP'))  
    df_sample = pl.read_parquet("tests/sample_data/polars_COTAHIST_A2024.ZIP.parquet")
    polars_assert(b3_data, df_sample)
    