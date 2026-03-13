IF OBJECT_ID('dbo.raw_market_data', 'U') IS NOT NULL
    DROP TABLE dbo.raw_market_data;

IF OBJECT_ID('dbo.clean_market_data', 'U') IS NOT NULL
    DROP TABLE dbo.clean_market_data;
GO

CREATE TABLE dbo.raw_market_data (
    symbol NVARCHAR(20) NOT NULL,
    trade_date DATE NOT NULL,
    open_price DECIMAL(18,6) NULL,
    high_price DECIMAL(18,6) NULL,
    low_price DECIMAL(18,6) NULL,
    close_price DECIMAL(18,6) NULL,
    adjusted_close DECIMAL(18,6) NULL,
    volume BIGINT NULL
);
GO

CREATE TABLE dbo.clean_market_data (
    symbol NVARCHAR(20) NOT NULL,
    trade_date DATE NOT NULL,
    open_price DECIMAL(18,6) NULL,
    high_price DECIMAL(18,6) NULL,
    low_price DECIMAL(18,6) NULL,
    close_price DECIMAL(18,6) NULL,
    adjusted_close DECIMAL(18,6) NULL,
    volume BIGINT NULL,
    return_1d FLOAT NULL,
    ma_7 DECIMAL(18,6) NULL,
    ma_30 DECIMAL(18,6) NULL,
    volatility_7d FLOAT NULL
);
GO