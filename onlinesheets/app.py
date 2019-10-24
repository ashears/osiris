from fastapi import FastAPI, APIRouter
from typing import List
from pydantic import BaseModel


class OnlineSheets(FastAPI):
    def __init__(self,
                 database_path: str,
                 tables: List[BaseModel]):
        self.database_path = database_path

        for table_model in tables:
            # Audit the sqlitedb
            self.create_router(table_model)

    def create_router(self, table_model: BaseModel):
        table_name = table_model.__name__
        fields = table_model.__dict__.get('__fields').keys()
        router = APIRouter()

        @router.get("/")
        def get_table():
            pass

        @router.post("/")
        def insert_entry(entry: table_model = Body(...)):  # TODO: Validate that the table_model here is a valid way to do this.
            pass

        @router.delete("/{id}")
        def delete_entry_by_id(id: int):
            pass

        # TODO: Try to find a way to make a dynamic query args get

        self.include_router(router, prefix=table_name, tags=[table_name])
