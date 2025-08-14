"""constring builder.

ini adalah connection string builder yang akan secara runtime di input oleh user.
stored connection strings ini akan di simpan encrypted.
"""

from enum import StrEnum

from pydantic import BaseModel, Field


class AuthEnum(StrEnum):
    WINDOWS = "Windows"
    SQL = "SQL"


class Constring(BaseModel):
    model_config = {"from_attributes": True, "str_strip_whitespace": True}

    server: str
    database: str
    auth: AuthEnum
    username: str | None = None
    password: str | None = None
    encrypted: bool | None = Field(
        default=False, description="If True, the connection string is encrypted."
    )
    trusted: bool | None = Field(
        default=False, description="If True, Windows Authentication is used."
    )
    driver: str = Field(
        default="ODBC Driver 17 for SQL Server", description="The ODBC driver to use."
    )


def build_constring(con: Constring) -> str:
    """Build a SQL Server connection string from a Constring model.

    Args:
        con (Constring): Connection string model
    Returns:
        str: Connection string
    """
    driver = con.driver or "ODBC Driver 17 for SQL Server"
    if con.auth == AuthEnum.WINDOWS or con.trusted:
        return f"DRIVER={{{driver}}};SERVER={con.server};DATABASE={con.database};Trusted_Connection=yes;"
    elif con.auth == AuthEnum.SQL:
        if not con.username or not con.password:
            raise ValueError("Username and password required for SQL Authentication.")
        return f"DRIVER={{{driver}}};SERVER={con.server};DATABASE={con.database};UID={con.username};PWD={con.password};"
    else:
        raise ValueError("Invalid authentication type.")
