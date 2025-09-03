# Inistock Trend Project 🚀

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/username/inistock-trend-project)

The **Inistock Trend Project** is an automated tool for analyzing stock trends on the **Indonesia Stock Exchange (IDX)**.  
It uses historical data, technical indicators, and the **Kalman Filter** algorithm to determine stock trends and saves the results in **Excel** format.

---

## 🔑 Key Features

- **Automated Data Retrieval:** Automatically fetch stock data using `yfinance`.
- **Multi-Method Trend Analysis:** Uses 3 different approaches:
  1. **Moving Average (MA):** Compares closing price with MA.
  2. **Relative Strength Index (RSI):** Measures momentum using 14-day RSI.
  3. **Kalman Filter:** Predicts price trends with the Kalman Filter algorithm.
- **Overall Trend Determination:** Combines results from all three methods to generate a final trend (`Bullish`, `Bearish`, `Mixed`).
- **Model Validation:** Evaluates Kalman Filter accuracy using **Mean Squared Error (MSE)**.
- **Structured Output:** Saves analysis results to `Output_Trend.xlsx` with columns **Stock**, **Overall Trend**, **Buy**, **Target**, and **Stop Loss**.

---

## 📂 Project Structure

inistock_trend_project/
│── data/
│ └── stocks_name.xlsx    # List of stocks to process
│
│── utils/
│ ├── kalman_utils.py     # Kalman Filter tuning functions
│ ├── indicators.py       # Technical indicator calculations (RSI)
│ ├── rounding.py         # Stock price rounding according to tick size
│
│── core/
│ ├── stock_processor.py  # Main logic for processing a single stock
│
│── main.py               # Main script to run the project
│── requirements.txt      # Required Python libraries
│── README.md             # Project documentation---

---

## ⚙️ Requirements

Python 3.6+ and the following libraries (install via `requirements.txt`):

```bash
pip install pandas yfinance scikit-learn pykalman openpyxl

▶️ How to Use

1. Prepare stocks_name.xlsx in the data/ directory.

   Ensure it has a column stocks_name containing the stock tickers.

2. Install required libraries:

   pip install -r requirements.txt

3. Run the main script:

   python main.py

---

## Output Results

After the script finishes, a file named `Output_Trend.xlsx` will be created in the main directory. This file contains a table with the following columns:

| Stock | Overall_Trend | Buy | Target_Price | Stop_Loss |
| :---: | :-----------: | :-: | :----------: | :-------: |
| BISI | Bullish | 945 | 990 | 900 |
| IKAN | Bullish | 66 | 69 | 63 |
| WTON | Bullish | 88 | 92 | 84 |

---
