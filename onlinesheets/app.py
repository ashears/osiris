from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

class OnlineSheets():
    def __init__(self,
                 tables: List[BaseModel]):
        self.app = FastAPI()
        self.db

    pass