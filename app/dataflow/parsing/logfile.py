import re
import pandas as pd

from .parser import Parser


class LogFileParser(Parser):
    def parse(self) -> pd.DataFrame:
        ...

