import polars as pl
from .b3parser_base import B3ParserBase


class B3ParserPolars(B3ParserBase):
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
        meta_data = super()._load_meta_data()
        file = super()._load_file(file_path, file_type)
        df = pl.read_csv(file, has_header=False, skip_rows=1, new_columns=["full_str"])

        # Calculate slice values from widths.
        slice_tuples = []
        offset = 0

        for i in meta_data['sizes']:
            slice_tuples.append((offset, i))
            offset += i

        df = df.with_columns(
            [
            pl.col("full_str").str.slice(slice_tuple[0], slice_tuple[1]).str.strip_chars().alias(col)
            for slice_tuple, col in zip(slice_tuples, meta_data['names'])
            ]
        ).drop("full_str")

        return df
