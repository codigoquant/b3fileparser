import os
import pandas as pd

from b3fileparser.b3parser import B3Parser


parser = B3Parser.create_parser('pandas')

def get_path(name):
    return os.path.join(os.path.dirname(__file__), "sample_data", name)

def test_txt_file():
    b3_data = parser.read_b3_file(get_path('COTAHIST_A2023_test.TXT'))
    df_sample = pd.read_pickle("tests/sample_data/sample_2023.pkl", compression={'method': 'gzip'})
    pd.testing.assert_frame_equal(b3_data, df_sample)

def test_data():
    b3_data =  parser.read_b3_file(get_path('COTAHIST_A2024.ZIP'))  
    df_sample = pd.read_pickle("tests/sample_data/sample_2024.pkl", compression={'method': 'gzip'})
    pd.testing.assert_frame_equal(b3_data, df_sample)