from .b3parser_base import B3ParserBase
import pandas as pd


class B3ParserPandas(B3ParserBase):
    def read_b3_file(self, file_path, file_type='path') -> pd.DataFrame:
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
        meta_data = super()._load_meta_data()
        file = super()._load_file(file_path, file_type)        

        # Read and parse the file
        b3_data = pd.read_fwf(
            file,
            header=None,
            names=meta_data['names'],
            widths=meta_data['sizes'],
            dtype=meta_data['dtypes'],        
            encoding='latin1',
        )[1:-1]  # Skip potential header and footer rows

        # Post-process the data
        b3_data = self._post_processing(b3_data, meta_data)    
        return b3_data
    
    def _post_processing(self, df, meta_data):
        for col in df.columns:
            if ('PRECO_' in col or 'VOLUME' in col):
                df[col] = df[col] / 100
            if 'DATA' in col:
                df[col] = df[col].apply(lambda x: pd.NaT if x == "99991231" else x )
                df[col] = pd.to_datetime(df[col])         
            if col == "TIPO_DE_MERCADO":
                df[col] = df[col].apply(lambda x: meta_data["MARKETS"].get(x, x))
            if col == "INDICADOR_DE_CORRECAO_DE_PRECOS":
                df[col] = df[col].apply(lambda x: meta_data["INDOPC"].get(x, x))
            if col == "CODIGO_BDI":
                df[col] = df[col].apply(lambda x: meta_data["CODBDI"].get(x, x))
        return df

