from b3fileparser import b3parser, b3_meta_data
import os
import pandas as pd

def get_path(name):
    return os.path.join(os.path.dirname(__file__), "sample_data", name)

def test_zip_file():
    dados_b3 = b3parser.read_b3_file(get_path('COTAHIST_A2024.ZIP'))    
    assert dados_b3 is not None

def test_txt_file():
    dados_b3 = b3parser.read_b3_file(get_path('COTAHIST_A2023_test.TXT'))
    print(dados_b3)
    assert dados_b3 is not None

def test_data():
    dados_b3 = b3parser.read_b3_file(get_path('COTAHIST_A2024.ZIP'))    
    meta_data = pd.DataFrame(data=b3_meta_data.META_DATA.values())
    dtypes = {row[1]:row[2] for row in meta_data[['name','dtype']].itertuples()}
    df_sample = pd.read_csv(get_path('sample.zip'), index_col=0, parse_dates=["DATA_DO_PREGAO", "DATA_DE_VENCIMENTO"],  dtype=dtypes)
    df_sample = b3parser._post_processing(df_sample, divide_by_100=False)
    pd.testing.assert_frame_equal(dados_b3, df_sample, check_dtype=False, check_categorical=False)