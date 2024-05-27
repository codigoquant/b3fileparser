import polars as pl
from b3fileparser.b3parser_base import B3ParserBase
from typing import Dict, Tuple
from pathlib import Path
import b3fileparser.b3_meta_data as meta_data


class B3ParserPolars(B3ParserBase):
    def _read_fixed_width_file_as_strs(self, file_path: Path | str, col_names_and_widths: Dict[str, int], skip_rows: int = 0) -> pl.DataFrame:
        """
        Reads a fixed-width file into a dataframe.
        Reads all values as strings.
        Strips all values of leading/trailing whitespaces.

        Args:
            col_names_and_widths: A dictionary where the keys are the column names and the values are the widths of the columns.
        """
        df = pl.read_csv(
            file_path,
            has_header=False,
            skip_rows=skip_rows,
            new_columns=["full_str"],
            encoding='latin1'
        )

        # transform col_names_and_widths into a Dict[cols name, Tuple[start, width]]
        slices: Dict[str, Tuple[int, int]] = {}
        start = 0
        for col_name, width in col_names_and_widths.items():
            slices[col_name] = (start, width)
            start += width

        df = df.with_columns(
            [
                pl.col("full_str").str.slice(slice_tuple[0], slice_tuple[1]).str.strip_chars().alias(col)
                for col, slice_tuple in slices.items()
            ]
        ).drop(["full_str"])

        return df
        
    def read_b3_file(self, file_path, file_type='path') -> pl.DataFrame:
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

        df = self._read_fixed_width_file_as_strs(
            file_path=file, 
            col_names_and_widths=meta_data.FIELD_SIZES, 
            skip_rows=1
        )[:-1] # Skip the last row

        df = df.with_columns(
            pl.col(meta_data.DATE_COLUMNS).str.to_date(format="%Y%m%d"),
            pl.col(meta_data.FLOAT32_COLUMNS).cast(pl.Float32) / 100,
            pl.col(meta_data.FLOAT64_COLUMNS).cast(pl.Float64),
            pl.col(meta_data.UINT32_COLUMNS).cast(pl.UInt32, strict=False),
            pl.col("CODIGO_BDI").map_elements(lambda x: meta_data.CODBDI.get(x, x), return_dtype=str),
            pl.col("TIPO_DE_MERCADO").map_elements(lambda x: meta_data.MARKETS.get(x, x), return_dtype=str),
            pl.col("INDICADOR_DE_CORRECAO_DE_PRECOS").map_elements(lambda x: meta_data.INDOPC.get(x, x), return_dtype=str),
        )
        
        return df
    