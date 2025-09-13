import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# --- CONFIG ---
ticker = "AAPL"           # change to any ticker you want
period = "6mo"
interval = "1d"
window = 20               # Bollinger window

# --- 1. Download data (explicit auto_adjust to avoid FutureWarning) ---
data = yf.download(ticker, period=period, interval=interval, auto_adjust=False, progress=False)
if data.empty:
    raise SystemExit("No data downloaded. Check ticker/network.")

# --- 2. Flatten MultiIndex columns (if present) so we always have single-level names) ---
if isinstance(data.columns, pd.MultiIndex):
    data.columns = ['_'.join([str(x) for x in col if x is not None and str(x) != '']).strip() for col in data.columns]

# --- 3. Find the Close column robustly (handles 'Close', 'Close_AAPL', 'AAPL_Close', etc.) ---
close_candidates = [c for c in data.columns if 'close' in c.lower()]
if not close_candidates:
    raise SystemExit(f"No 'Close' column found. Columns: {list(data.columns)}")
# prefer exact match if exists, otherwise take the first candidate
close_col = next((c for c in close_candidates if c.lower() == 'close'), close_candidates[0])
close = data[close_col].astype(float)

# --- 4. Compute Bollinger Bands using that close series ---
data['MA20'] = close.rolling(window=window).mean()
data['STD20'] = close.rolling(window=window).std()
data['Upper'] = data['MA20'] + 2 * data['STD20']
data['Lower'] = data['MA20'] - 2 * data['STD20']

# --- 5. Work only on rows where bands exist (drop NaNs from rolling) ---
working = data.dropna(subset=['MA20','STD20','Upper','Lower']).copy()
close_w = working[close_col]   # aligned Series

# --- 6. Generate signals (comparison is now between aligned Series) ---
working['Signal'] = 'HOLD'
working.loc[close_w <= working['Lower'], 'Signal'] = 'BUY'
working.loc[close_w >= working['Upper'], 'Signal'] = 'SELL'

# --- 7. Plot price, bands and BUY/SELL markers ---
plt.figure(figsize=(14,7))
plt.plot(working.index, close_w, label="Close Price", linewidth=1.2)
plt.plot(working.index, working['MA20'], label="20-day MA", linewidth=1.0)
plt.plot(working.index, working['Upper'], linestyle='--', label="Upper Band")
plt.plot(working.index, working['Lower'], linestyle='--', label="Lower Band")

# markers
buys = working[working['Signal'] == 'BUY']
sells = working[working['Signal'] == 'SELL']
plt.scatter(buys.index, buys[close_col], marker='^', s=100, label='BUY', zorder=5)
plt.scatter(sells.index, sells[close_col], marker='v', s=100, label='SELL', zorder=5)

# axis formatting
plt.title(f"{ticker} — Bollinger Bands & Signals")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 8. Print last rows with signals ---
print(working[[close_col, 'MA20', 'Upper', 'Lower', 'Signal']].tail(15))
