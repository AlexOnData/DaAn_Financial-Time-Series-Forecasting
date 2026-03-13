from extract_yfinance import extract_all_symbols, save_raw_data
from transform_market_data import transform_market_data, save_processed_data
from load_to_azure import run_load


def main():
    print("Step 1: Extracting raw market data...")
    raw_df = extract_all_symbols()
    save_raw_data(raw_df)

    print("\nStep 2: Transforming market data...")
    processed_df = transform_market_data()
    save_processed_data(processed_df)

    print("\nStep 3: Loading data into Azure SQL...")
    run_load()

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()