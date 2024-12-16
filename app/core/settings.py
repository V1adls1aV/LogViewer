from pydantic import BaseModel
from functools import lru_cache
from os import environ as env
from dotenv import load_dotenv
import yaml

class Config(BaseModel):
    ENCODING: str
    SEGMENT_COUNT: int


@lru_cache()
def get_config(filename='config.yaml') -> Config:
    load_dotenv()

    with open(filename, 'r') as file:
        return Config(
            **yaml.safe_load(file),
            **dict(env))


config = get_config()
