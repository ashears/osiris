from fastapi import FastAPI, APIRouter
from typing import List
from pydantic import BaseModel


class Table(BaseModel):
    table_name: str
    table: BaseModel



def process_tables(tables: List[BaseModel]):
    for table in tables:
        create_router(table)
        pass
        # Create the fastapi portion
        # 1. add


class OnlineSheets:
    def __init__(self,
                 tables: List[BaseModel]):
        self.app = FastAPI()
        # self.db

        process_tables(tables)

    def create_router(self, table: Table):
        router = APIRouter()

        @router.get("/")
        def get_table():
            pass

        @router.post("/")
        def insert_entry():
            pass

        @router.delete("/{id}")
        def delete_entry_by_id(id: int):
            pass

        # TODO: Try to find a way to make a dynamic query args get

        self.app.include_router(router, prefix=table.table_name)

    pass