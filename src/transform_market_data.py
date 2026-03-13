import pandas as pd

from config import RAW_FILE_PATH, PROCESSED_FILE_PATH


def transform_market_data() -> pd.DataFrame:
    """
    Read raw daily market data and create engineered features.
    """
    df = pd.read_csv(RAW_FILE_PATH)

    df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date

    numeric_columns = [
        "open_price",
        "high_price",
        "low_price",
        "close_price",
        "adjusted_close",
        "volume"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.drop_duplicates(subset=["symbol", "trade_date"]).copy()
    df = df.sort_values(["symbol", "trade_date"]).reset_index(drop=True)

    grouped = df.groupby("symbol", group_keys=False)

    df["return_1d"] = grouped["adjusted_close"].pct_change()
    df["ma_7"] = grouped["adjusted_close"].transform(lambda s: s.rolling(7).mean())
    df["ma_30"] = grouped["adjusted_close"].transform(lambda s: s.rolling(30).mean())
    df["volatility_7d"] = grouped["return_1d"].transform(lambda s: s.rolling(7).std())

    return df


def save_processed_data(df: pd.DataFrame) -> None:
    """
    Save processed data to CSV.
    """
    df.to_csv(PROCESSED_FILE_PATH, index=False)
    print(f"Processed data saved to: {PROCESSED_FILE_PATH}")


if __name__ == "__main__":
    processed_df = transform_market_data()
    save_processed_data(processed_df)