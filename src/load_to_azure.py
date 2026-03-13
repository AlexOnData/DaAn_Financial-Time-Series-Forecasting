import os
import urllib.parse
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from config import RAW_FILE_PATH, PROCESSED_FILE_PATH

load_dotenv()


def get_engine():
    """
    Create SQLAlchemy engine for Azure SQL Database.
    """
    server = os.getenv("SQL_SERVER")
    database = os.getenv("SQL_DATABASE")
    username = os.getenv("SQL_USERNAME")
    password = os.getenv("SQL_PASSWORD")

    if not all([server, database, username, password]):
        raise ValueError("Missing one or more SQL connection values in .env")

    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    params = urllib.parse.quote_plus(connection_string)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

    return engine


def truncate_table(engine, table_name: str) -> None:
    """
    Truncate table before reloading data.
    """
    with engine.begin() as conn:
        conn.execute(text(f"TRUNCATE TABLE {table_name};"))
    print(f"Table truncated: {table_name}")


def load_csv_to_table(engine, csv_path: str, table_name: str) -> None:
    """
    Load CSV file into Azure SQL table.
    """
    df = pd.read_csv(csv_path)

    if "trade_date" in df.columns:
        df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False,
        chunksize=500,
        method=None
    )

    print(f"Loaded {len(df)} rows into {table_name}")


def run_load():
    engine = get_engine()

    truncate_table(engine, "raw_market_data")
    truncate_table(engine, "clean_market_data")

    load_csv_to_table(engine, str(RAW_FILE_PATH), "raw_market_data")
    load_csv_to_table(engine, str(PROCESSED_FILE_PATH), "clean_market_data")


if __name__ == "__main__":
    run_load()