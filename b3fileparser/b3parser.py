import pandas as pd
from b3fileparser import b3_meta_data
from zipfile import ZipFile
from io import BytesIO
import os

def read_b3_file(file_path, file_type='path'):
    """
    Reads financial data from a Brazilian B3 file, supporting both plaintext and zipped formats.

    Parameters:
        file_path (str): Path or bytes of the file to be read.
        file_type (str): 'path' if `file_path` is a filesystem path, 'bytes' if `file_path` is bytes data.

    Returns:
        pandas.DataFrame: Parsed data as a DataFrame, or None if an error occurs.

    Raises:
        ValueError: If the file format is not supported or `file_type` is invalid.

    Examples:
        # Read data from a TXT file
        df = read_b3_file('/path/to/file.TXT')

        # Read data from a ZIP file containing a TXT file
        df = read_b3_file('/path/to/file.ZIP')

        # Read data from bytes
        df = read_b3_file(b'raw binary data from file', file_type='bytes')
    """
    # Validate the file type parameter
    if file_type not in ['path', 'bytes']:
        raise ValueError("Invalid file_type specified. Choose 'path' or 'bytes'.")

    # Prepare columns and their sizes based on metadata
    columns = [info['name'] for info in b3_meta_data.META_DATA.values()]
    size_fields = [info['size'] for info in b3_meta_data.META_DATA.values()]

    # Handle file input based on type
    if file_type == 'path':
        if not file_path.lower().endswith(('.txt', '.zip')):
            raise ValueError('Invalid file format! Provide a .TXT or .ZIP file containing a .TXT')
        
        if file_path.lower().endswith('.zip'):
            with ZipFile(file_path, 'r') as file_zip:
                # Assuming the TXT file has the same base name as the ZIP file
                txt_filename = os.path.basename(file_path).replace('.ZIP', '.TXT')
                file = BytesIO(file_zip.read(txt_filename))
        else:
            file = file_path

    elif file_type == 'bytes':
        file = BytesIO(file_path)

    # Read and parse the file
    b3_data = pd.read_fwf(
        file,
        widths=size_fields,
        header=None,
        names=columns,
        encoding='latin1'
    )[1:-1]  # Skip potential header and footer rows

    # Post-process the data
    for col in columns:
        if 'PRECO' in col or 'VOLUME' in col:
            b3_data[col] = b3_data[col] / 100
        if 'DATA' in col:
            b3_data[col] = pd.to_datetime(b3_data[col], errors='coerce')
        if col in ["CODIGO_BDI", "PRAZO_EM_DIAS_DO_MERCADO_A_TERMO", "NUMERO_DE_DISTRIBUICAO", "FATOR_DE_COTACAO", 'INDICADOR_DE_CORRECAO_DE_PRECOS']:
            b3_data[col] = b3_data[col].fillna(-1).astype(int)
        if col == "TIPO_DE_MERCADO":
            b3_data[col] = b3_data[col].apply(lambda x: b3_meta_data.MARKETS.get(x, "unknown"))
        if col == "INDICADOR_DE_CORRECAO_DE_PRECOS":
            b3_data[col] = b3_data[col].apply(lambda x: b3_meta_data.INDOPC.get(x, "unknown"))
        if col == "CODIGO_BDI":
            b3_data[col] = b3_data[col].apply(lambda x: b3_meta_data.CODBDI.get(x, "unknown"))

    return b3_data
