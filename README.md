# 📊 Financial Time Series Forecasting
*Python | SQL Server | Power BI*

## 🔹 Project Overview
This project aims to explore financial time series forecasting using Python, SQL Server, and Power BI.  
It is currently in the planning stage, focusing on designing a pipeline for data collection, modeling (Prophet and ARIMA), and interactive visualization.  

The project will demonstrate end-to-end integration of **data analysis, machine learning, and business intelligence**, and serve as a portfolio-ready example of applied financial analytics.

---

# Financial Time Series Forecasting Project

## Objective
This project extracts daily market data for:
- AAPL
- NVDA
- ^GSPC

The time range starts at:
- 2005-01-01

The pipeline only keeps data up to:
- yesterday

## Pipeline
1. Extract raw daily data from Yahoo Finance
2. Transform and engineer features
3. Load data into Azure SQL Database
4. Connect Power BI to Azure SQL for reporting

## Run the project

```bash
python src/main.py
```
---

# How to run everything

From the project root:

```bash
python src/main.py
```

# What will do all 3 steps:

extract
transform
load