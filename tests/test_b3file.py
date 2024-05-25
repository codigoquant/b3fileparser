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

def test_txt_file_pandas():
    b3_data = parser_pandas.read_b3_file(get_path('COTAHIST_A2023_test.TXT'))
    df_sample = pd.read_pickle("tests/sample_data/sample_2023.pkl", compression={'method': 'gzip'})
    pandas_assert(b3_data, df_sample)

def test_zip_file_pandas():
    b3_data =  parser_pandas.read_b3_file(get_path('COTAHIST_A2024.ZIP'))  
    df_sample = pd.read_pickle("tests/sample_data/sample_2024.pkl", compression={'method': 'gzip'})
    pandas_assert(b3_data, df_sample)

def test_txt_file_polars():
    b3_data = parser_polars.read_b3_file(get_path('COTAHIST_A2023_test.TXT'))
    df_sample = pl.read_parquet(get_path('sample_2023.parquet'))
    polars_assert(b3_data, df_sample)

def test_zip_file_polars():
    b3_data =  parser_polars.read_b3_file(get_path('COTAHIST_A2024.ZIP'))  
    df_sample = pl.read_parquet(get_path('sample_2024.parquet'))
    polars_assert(b3_data, df_sample)
    