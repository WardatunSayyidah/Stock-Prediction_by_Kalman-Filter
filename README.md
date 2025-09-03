# Inistock Trend Project

This project is an automated tool for analyzing stock trends on the Indonesia Stock Exchange (IDX). By using historical data, this project applies various technical indicators and the Kalman Filter algorithm to determine the overall trend of each stock, then saves the results in an Excel file format.

---

## Key Features

* **Automated Data Retrieval:** Uses the `yfinance` library to download historical stock data.
* **Multi-Method Trend Analysis:** Analyzes stock trends using three different approaches:
    1.  **Moving Average (MA):** Compares the closing price with MA.
    2.  **Relative Strength Index (RSI):** Measures momentum with a 14-day RSI.
    3.  **Kalman Filter:** Uses the Kalman Filter to predict price trends.
* **Overall Trend Determination:** Combines the results of the three methods to determine the final trend (`Bullish`, `Bearish`, or `Mixed`).
* **Model Validation:** Measures the accuracy of the Kalman Filter model using Mean Squared Error (MSE) to ensure consistency and reliability.
* **Structured Output:** Saves the analysis results to an `Output_Trend.xlsx` file containing the stock name, overall trend, and recommended `Buy`, `Target`, and `Stop Loss` prices.

---

## Project Structure

inistock_trend_project/
│── data/
│   └── stocks_name.xlsx     # List of stock names to be processed
│
│── utils/
│   ├── kalman_utils.py      # Function for tuning the Kalman Filter
│   ├── indicators.py        # Function for computing technical indicators (RSI)
│   ├── rounding.py          # Function for rounding stock prices according to tick size
│
│── core/
│   ├── stock_processor.py   # Main logic for processing a single stock
│
│── main.py                  # Main script to run the entire process
│── requirements.txt         # List of required libraries
│── README.md                # Project documentation

---

## Requirements

This project requires Python 3.6+ and the following libraries, which can be installed from `requirements.txt`:
pandas
yfinance
scikit-learn
pykalman
openpyxl

---

## How to Use

1.  **Make sure your `stocks_name.xlsx` file is ready.** This file should be located in the `data/` directory and have a column named `stocks_name` that contains a list of stock tickers (e.g., `TLKM`, `BBCA`).
2.  **Install all necessary libraries** by running the following command in your terminal:
    ```
    pip install -r requirements.txt
    ```
3.  **Run the main script** from the project directory:
    ```
    python main.py
    ```

---

## Output Results

After the script finishes, a file named `Output_Trend.xlsx` will be created in the main directory. This file contains a table with the following columns:

| Stock | Overall_Trend | Buy | Target_Price | Stop_Loss |
| :---: | :-----------: | :-: | :----------: | :-------: |
| BISI | Bullish | 945 | 990 | 900 |
| IKAN | Bullish | 66 | 69 | 63 |
| WTON | Bullish | 88 | 92 | 84 |

---
