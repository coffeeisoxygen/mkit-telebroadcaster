import pytest
from src.database.constring import build_constring


def test_build_constring_windows_auth():
    result = build_constring(
        server="localhost", database="testdb", use_windows_auth=True
    )
    assert result == (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=testdb;"
        "Trusted_Connection=yes;"
    )


def test_build_constring_sql_auth_success():
    result = build_constring(
        server="localhost",
        database="testdb",
        use_windows_auth=False,
        username="user",
        password="pass",
    )
    assert result == (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=testdb;"
        "UID=user;"
        "PWD=pass;"
    )


def test_build_constring_sql_auth_missing_username():
    with pytest.raises(ValueError):
        build_constring(
            server="localhost",
            database="testdb",
            use_windows_auth=False,
            password="pass",
        )


def test_build_constring_sql_auth_missing_password():
    with pytest.raises(ValueError):
        build_constring(
            server="localhost",
            database="testdb",
            use_windows_auth=False,
            username="user",
        )
