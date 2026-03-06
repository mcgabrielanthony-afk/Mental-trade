import pandas as pd
import numpy as np

# Calculate Relative Strength Index (RSI)
def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calculate Moving Average Convergence Divergence (MACD)
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_window, adjust=False).mean()
    return macd, signal

# Calculate Bollinger Bands

def calculate_bollinger_bands(data, window=20):
    rolling_mean = data['Close'].rolling(window=window).mean()
    rolling_std = data['Close'].rolling(window=window).std()
    upper_band = rolling_mean + (rolling_std * 2)
    lower_band = rolling_mean - (rolling_std * 2)
    return upper_band, lower_band

# Calculate Moving Averages

def calculate_moving_average(data, window=50):
    return data['Close'].rolling(window=window).mean()

# Example Usage:
# df = pd.read_csv('your_data.csv')  # Load DataFrame containing stock data
# df['RSI'] = calculate_rsi(df)
# df['MACD'], df['Signal'] = calculate_macd(df)
# df['Upper_Band'], df['Lower_Band'] = calculate_bollinger_bands(df)
# df['Moving_Average'] = calculate_moving_average(df)