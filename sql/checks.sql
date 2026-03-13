SELECT symbol, MIN(trade_date) AS min_date, MAX(trade_date) AS max_date, COUNT(*) AS row_count
FROM dbo.raw_market_data
GROUP BY symbol
ORDER BY symbol;

SELECT TOP 20 *
FROM dbo.clean_market_data
ORDER BY symbol, trade_date DESC;