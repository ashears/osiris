from pydantic import BaseModel
from onlinesheets import OnlineSheets
import requests


class Dogs(BaseModel):
    dog_name: str
    dog_breed: str
    dog_color: str
    dog_age: int


class Cats(BaseModel):
    cat_name: str
    cat_color: str
    cat_age: int


app = OnlineSheets(database_path="database.db", tables=[Cats, Dogs])

if __name__ == '__main__':
    pass
