import pandas as pd
import yfinance as yf

from config import SYMBOLS, START_DATE, TODAY, YESTERDAY, RAW_FILE_PATH


def flatten_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Flatten MultiIndex columns if they appear.
    """
    df.columns = [col[0] if isinstance(col, tuple) else col for col in df.columns]
    return df


def download_symbol_data(symbol: str) -> pd.DataFrame:
    """
    Download daily market data for one symbol from Yahoo Finance.
    """
    df = yf.download(
        tickers=symbol,
        start=START_DATE,
        end=TODAY.strftime("%Y-%m-%d"),
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    if df.empty:
        raise ValueError(f"No data returned for symbol: {symbol}")

    df = df.reset_index()
    df = flatten_columns(df)

    rename_map = {
        "Date": "trade_date",
        "Open": "open_price",
        "High": "high_price",
        "Low": "low_price",
        "Close": "close_price",
        "Adj Close": "adjusted_close",
        "Volume": "volume"
    }

    df = df.rename(columns=rename_map)

    required_columns = [
        "trade_date",
        "open_price",
        "high_price",
        "low_price",
        "close_price",
        "adjusted_close",
        "volume"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing expected columns for {symbol}: {missing_columns}")

    df = df[required_columns].copy()
    df["symbol"] = symbol

    df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date
    df = df[df["trade_date"] <= YESTERDAY].copy()

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

    df = df.sort_values("trade_date").reset_index(drop=True)

    return df


def extract_all_symbols() -> pd.DataFrame:
    """
    Download data for all configured symbols and combine them into one DataFrame.
    """
    all_frames = []

    for symbol in SYMBOLS:
        print(f"Downloading data for {symbol}...")
        symbol_df = download_symbol_data(symbol)
        print(
            f"{symbol}: {len(symbol_df)} rows | "
            f"{symbol_df['trade_date'].min()} -> {symbol_df['trade_date'].max()}"
        )
        all_frames.append(symbol_df)

    final_df = pd.concat(all_frames, ignore_index=True)
    final_df = final_df.sort_values(["symbol", "trade_date"]).reset_index(drop=True)

    return final_df


def save_raw_data(df: pd.DataFrame) -> None:
    """
    Save raw extracted data to CSV.
    """
    df.to_csv(RAW_FILE_PATH, index=False)
    print(f"Raw data saved to: {RAW_FILE_PATH}")


if __name__ == "__main__":
    raw_df = extract_all_symbols()
    save_raw_data(raw_df)