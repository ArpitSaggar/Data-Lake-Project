from pathlib import Path
import duckdb
import pandas as pd

project_root = Path(__file__).resolve().parent.parent
gold = project_root / "gold"

con = duckdb.connect()


def load_page():
    return con.execute(
        f"SELECT * FROM read_parquet('{gold}/page_analytics/*.parquet')"
    ).df()


def load_device():
    return con.execute(
        f"SELECT * FROM read_parquet('{gold}/device_analytics/*.parquet')"
    ).df()


def load_browser():
    return con.execute(
        f"SELECT * FROM read_parquet('{gold}/browser_analytics/*.parquet')"
    ).df()


def load_category():
    return con.execute(
        f"SELECT * FROM read_parquet('{gold}/category_analytics/*.parquet')"
    ).df()


def load_referral():
    return con.execute(
        f"SELECT * FROM read_parquet('{gold}/traffic_analytics/*.parquet')"
    ).df()


def load_purchase():
    return con.execute(
        f"SELECT * FROM read_parquet('{gold}/purchase_analytics/*.parquet')"
    ).df()


def load_os():
    return con.execute(
        f"SELECT * FROM read_parquet('{gold}/os_analytics/*.parquet')"
    ).df()