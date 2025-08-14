"""constring builder.

ini adalah connection string builder yang akan secara runtime di input oleh user.
stored connection strings ini akan di simpan encrypted.
"""

from typing import Optional


def build_constring(
    server: str,
    database: str,
    use_windows_auth: bool,
    username: Optional[str] = None,
    password: Optional[str] = None,
) -> str:
    """
    Build a SQL Server connection string for either Windows or SQL Authentication.
    Args:
            server (str): SQL Server address
            database (str): Database name
            use_windows_auth (bool): True for Windows Auth, False for SQL Auth
            username (str, optional): SQL username (required for SQL Auth)
            password (str, optional): SQL password (required for SQL Auth)
    Returns:
            str: Connection string
    """
    if use_windows_auth:
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
    else:
        if not username or not password:
            raise ValueError("Username and password required for SQL Authentication.")
        return f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};"
