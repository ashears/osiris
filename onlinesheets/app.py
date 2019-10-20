from fastapi import FastAPI, APIRouter
from typing import List
from pydantic import BaseModel


class OnlineSheets:
    def __init__(self,
                 tables: List[BaseModel]):
        self.app = FastAPI()
        # self.db

        self.__process_tables(tables)

    def __process_tables(self, tables: List[BaseModel]):
        for table_model in tables:
            # Check whether required content is in the database
            # sqliteauditor.audit_database(db, tables=tables, validate_headers=True)

            self.create_router(table_model)

    def create_router(self, table_model):
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

        self.app.include_router(router, prefix=table_name)

    pass