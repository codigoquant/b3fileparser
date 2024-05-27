from abc import abstractmethod, ABC
from zipfile import ZipFile
from io import BytesIO
from typing import Dict
import os
import pandas as pd
import polars as pl


class B3ParserBase(ABC):
    def __init__(self) -> None:
        super().__init__()        
    
    @abstractmethod
    def read_b3_file(file_path: str, file_type: str) -> pd.DataFrame | pl.DataFrame: 
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
    @staticmethod    
    def _load_file(file_path: str, file_type: str) -> BytesIO:
        # Validate the file type parameter
        if file_type not in ['path', 'bytes']:
            raise ValueError("Invalid file_type specified. Choose 'path' or 'bytes'.")
        
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
        return file
