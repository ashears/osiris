from fastapi import FastAPI, APIRouter, Body
from typing import List
from pydantic import BaseModel
import sqlite3


class OnlineSheets(FastAPI):
    def __init__(self,
                 tables: List[BaseModel],
                 path_to_db: str = ""):
        self.app = FastAPI()
        self.create_database(path_to_db, tables)
        for table_model in tables:
            # Audit the sqlitedb
            # self.create_database(path_to_db, table_model)
            self.create_router(table_model)


    def create_router(self, table_model: BaseModel):
        table_name = table_model.__name__
        fields = table_model.__dict__.get('__fields__').keys()
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

        self.app.include_router(router, prefix=f"/{table_name}", tags=[table_name])

    def create_database(self, path_to_db: str, tables: List[BaseModel]):
        with sqlite3.connect(path_to_db + "onlinesheets.db") as conn:
            cursor = conn.cursor()

            for table_model in tables:
                qry = (f"CREATE TABLE IF NOT EXISTS {table_model.__name__} "
                       "(id INTEGER PRIMARY KEY")
                fields = table_model.__dict__.get('__fields__').keys()
                for field in fields:
                    qry += f", {field} TEXT"
                qry += ")"

                cursor.execute(qry)