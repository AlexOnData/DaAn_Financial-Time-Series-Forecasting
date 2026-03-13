from pathlib import Path
from datetime import datetime, timedelta

# -------------------------------
# General project configuration
# -------------------------------

SYMBOLS = ["AAPL", "NVDA", "^GSPC"]
START_DATE = "2005-01-01"

TODAY = datetime.today().date()
YESTERDAY = TODAY - timedelta(days=1)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

RAW_FILE_NAME = "all_symbols_daily_raw.csv"
PROCESSED_FILE_NAME = "all_symbols_daily_clean.csv"

RAW_FILE_PATH = RAW_DIR / RAW_FILE_NAME
PROCESSED_FILE_PATH = PROCESSED_DIR / PROCESSED_FILE_NAME