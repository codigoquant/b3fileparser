import pandas as pd
from b3fileparser import b3_meta_data
from zipfile import ZipFile
from io import BytesIO
import os

def read_b3_file(file_name):
    columns = []
    size_fields = []
    for col, info in b3_meta_data.META_DATA.items():
        columns.append(info['name'])
        size_fields.append(info['size'])

    if not (file_name.endswith('TXT') or file_name.endswith('ZIP')):
        print('Invalid format! Provide a .TXT or .ZIP file containing a .TXT')
        return
    
    if file_name.endswith('.ZIP'):
        with ZipFile(file_name, mode='r') as file_zip:                         
            file_name_txt = os.path.basename(file_name).replace('.ZIP', '.TXT')
            file = BytesIO(file_zip.read(file_name_txt))                      
        
    if file_name.endswith('.TXT'):
        file = file_name
   
    b3_data = pd.read_fwf(
        file,
        widths=size_fields,
        header=None,
        names=columns,
        encoding='latin1'
    )[1:-1]

    for col in columns:
        if col.startswith('PRECO') or col.startswith('VOLUME'):
            b3_data[col] = b3_data[col] / 100
        if col == "DATA_DE_VENCIMENTO":
            b3_data[col] = b3_data[col].astype(int).astype(str)
            b3_data[col] = pd.to_datetime(b3_data[col], errors='coerce')
        if col.startswith('DATA'):
            b3_data[col] = pd.to_datetime(b3_data[col])
        if col in ["CODIGO_BDI", "PRAZO_EM_DIAS_DO_MERCADO_A_TERMO", "NUMERO_DE_DISTRIBUICAO", "FATOR_DE_COTACAO", 'INDICADOR_DE_CORRECAO_DE_PRECOS']:
            b3_data[col] = b3_data[col].fillna(-1).astype(int)
        if col == "TIPO_DE_MERCADO":
            b3_data[col] = b3_data[col].apply(
                lambda x: b3_meta_data.MARKETS[x])
        if col == "INDICADOR_DE_CORRECAO_DE_PRECOS":
            b3_data[col] = b3_data[col].apply(lambda x: b3_meta_data.INDOPC.get(x, "sem_registro"))
        if col == "CODIGO_BDI":
            b3_data[col] = b3_data[col].apply(lambda x: b3_meta_data.CODBDI.get(x, "sem_registro"))

    return b3_data
