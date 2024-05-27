from b3fileparser.b3parser_base import B3ParserBase
import pandas as pd
import b3fileparser.b3_meta_data as meta_data


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
        file = super()._load_file(file_path, file_type)        

        # Read and parse the file
        df = pd.read_fwf(
            file,
            header=None,
            names=list(meta_data.FIELD_SIZES.keys()),
            widths=list(meta_data.FIELD_SIZES.values()),
            encoding='latin1',
        )[1:-1]  # Skip potential header and footer rows
        
        df["TIPO_DE_MERCADO"] = df["TIPO_DE_MERCADO"].apply(lambda x: meta_data.MARKETS.get(x, x))
        df["INDICADOR_DE_CORRECAO_DE_PRECOS"] = df["INDICADOR_DE_CORRECAO_DE_PRECOS"].apply(lambda x: meta_data.INDOPC.get(x, x))
        df["CODIGO_BDI"] = df["CODIGO_BDI"].apply(lambda x: meta_data.CODBDI.get(x, x))
        for col in meta_data.FLOAT32_COLUMNS: df[col] = df[col].astype(float) / 100
        for col in meta_data.FLOAT64_COLUMNS: df[col] = df[col].astype(float)
        for col in meta_data.DATE_COLUMNS:            
                df[col] = df[col].apply(lambda x: pd.NaT if x == "99991231" else x )
                df[col] = pd.to_datetime(df[col])

        return df

