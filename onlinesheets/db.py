from databases import Database
import hashlib


async def connect(path: str):
    database = Database(path)
    await database.connect()


def init_database(path: str, admin_pass: str):
    hashed = hashlib.sha256(admin_pass.encode()).hexdigest()
    query = "CREATE TABLE Users(user TEXT, pass TEXT)"
    await database.execute(query=query)
