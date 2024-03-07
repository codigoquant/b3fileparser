from b3fileparser import b3parser
import os

def get_path(name):
    return os.path.join(os.path.dirname(__file__), "sample_data", name)

def test_zip_file():
    dados_b3 = b3parser.read_b3_file(get_path('COTAHIST_A2024.ZIP'))    
    assert dados_b3 is not None

def test_txt_file():
    dados_b3 = b3parser.read_b3_file(get_path('COTAHIST_A2023_test.TXT'))
    print(dados_b3)
    assert dados_b3 is not None

    