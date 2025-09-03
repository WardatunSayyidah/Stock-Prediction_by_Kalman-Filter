import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pykalman import KalmanFilter

from utils.kalman_utils import tune_kalman_filter
from utils.indicators import compute_rsi
from utils.rounding import round_to_tick

def process_stock(stock_name):
    try:
        date_end = datetime(2025, 7, 7)
        date_start = date_end - timedelta(days=365)

        stock = yf.Ticker(stock_name)
        data = stock.history(start=date_start.strftime("%Y-%m-%d"), end=date_end.strftime("%Y-%m-%d"))
        splits = stock.splits

        if data.empty or not splits.empty or data['Close'].tail(10).nunique() == 1 or len(data) <= 200:
            return None, f"{stock_name.replace('.JK','')} dilewati (data tidak valid)."

        data = data.reset_index()
        data = data[data['Date'].dt.dayofweek < 5]

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[0] for col in data.columns]

        data = data[['Date', 'Close']].dropna()
        data.set_index('Date', inplace=True)
        data.index = data.index.strftime('%Y-%m-%d')

        # === Indikator Teknis (MA20 + RSI)
        data = data.sort_index()
        data['MA_20'] = data['Close'].rolling(window=20).mean()
        data['RSI_14'] = compute_rsi(data['Close'], period=14)

        # === Kalman Filter
        prices = data['Close']
        train_data, test_data = train_test_split(prices, test_size=0.2, shuffle=False)
        best_params = tune_kalman_filter(train_data)

        kf = KalmanFilter(
            initial_state_mean=train_data.iloc[0],
            observation_covariance=best_params['observation_covariance'],
            transition_covariance=best_params['transition_covariance'],
            transition_matrices=1,
            observation_matrices=1
        )
        state_means, _ = kf.filter(prices.values)

        # === Analisis Tren
        last_close = data['Close'].iloc[-1]
        last_ma20 = data['MA_20'].iloc[-1]
        last_rsi = data['RSI_14'].iloc[-1]

        if last_close > last_ma20:
            ma_trend = 'Bullish'
        elif last_close < last_ma20:
            ma_trend = 'Bearish'
        else:
            ma_trend = 'Neutral'

        if last_rsi < 40:
            rsi_trend = 'Bullish'
        elif last_rsi > 55:
            rsi_trend = 'Bearish'
        else:
            rsi_trend = 'Neutral'

        kalman_trend = 'Bullish' if state_means[-1] > state_means[-6] else 'Bearish'

        if ma_trend == rsi_trend == kalman_trend:
            overall_trend = kalman_trend
        else:
            overall_trend = 'Mixed'

        # === MSE Test
        predictions = state_means[-len(test_data):].flatten()
        mse_test = mean_squared_error(test_data, predictions)

        mse_acceptable = (
            (0 <= last_close < 5000 and mse_test < 0.1 * last_close) or
            (5000 <= last_close < 10000 and mse_test < 0.15 * last_close) or
            (10000 <= last_close < 20000 and mse_test < 0.2 * last_close) or
            (20000 <= last_close and mse_test < 0.25 * last_close)
        )

        # === Final Hasil
        if mse_acceptable and overall_trend in ['Bullish', 'Bearish']:
            close_price = int(round(data['Close'].iloc[-1]))
            buy = round_to_tick(close_price)
            target = round_to_tick(buy * 1.05)
            stop = round_to_tick(buy * 0.95)

            return {
                "Stock": stock_name.replace(".JK", ""),
                "Overall_Trend": overall_trend,
                "Buy": buy,
                "Target_Price": target,
                "Stop_Loss": stop
            }, f"{stock_name.replace('.JK','')}: Trend = {overall_trend}, MSE = {mse_test:.2f}"
        else:
            return None, f"{stock_name.replace('.JK','')} diabaikan (MSE/indikator tidak konsisten)."

    except Exception as e:
        return None, f"Failed to process {stock_name.replace('.JK','')} due to: {str(e)}"
