import sys
sys.path.append("../..")
from onlinesheets import OnlineSheets
from pydantic import SecretStr


class Users(BaseModel):
    username: str
    password: SecretStr


os = OnlineSheets(tables=[Users])

