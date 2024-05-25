from .b3parser_base import B3ParserBase
from .b3parser_pandas import B3ParserPandas
from .b3parser_polars import B3ParserPolars


class B3Parser():
    """B3Parser: Reads a b3 file and returns a DataFrame
    
        Example: 
            from b3fileparser.b3parser import B3Parser

            parser = B3Parser.create_parser('pandas')

            # Read data from a TXT file
            df = parser.read_b3_file('/path/to/file.TXT')

            # Read data from a ZIP file containing a TXT file
            df = parser.read_b3_file('/path/to/file.ZIP')

            # Read data from bytes
            df = parser.read_b3_file(b'raw binary data from file', file_type='bytes')
    """        

    @staticmethod    
    def create_parser(engine: str = "pandas") -> B3ParserBase:
        if engine == 'pandas':
            return B3ParserPandas()
        elif engine == 'polars':
            return B3ParserPolars()            
        else:
            raise Exception("engine parameter must be 'pandas' or 'polars'")
        