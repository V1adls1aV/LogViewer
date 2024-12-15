import abc
import pandas as pd
from io import StringIO


class Parser(abc.ABC):
    def __init__(self, data: StringIO) -> None:
        self.data = data

    @abc.abstractmethod
    def parse(self, fmt: str) -> pd.DataFrame:
        ...
