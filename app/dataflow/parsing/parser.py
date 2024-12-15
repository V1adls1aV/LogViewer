import abc
import pandas as pd
from io import StringIO


class Parser(abc.ABC):
    def __init__(self, data: StringIO) -> None:
        self.data = data

    @abc.abstractmethod
    def parse(self, format: str) -> pd.DataFrame:
        ...


from typing import Protocol

class UserData(Protocol):
    name: str
    age: int

    def get_age(self) -> int:
        ...
