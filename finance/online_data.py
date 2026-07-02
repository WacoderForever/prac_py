import yfinance as yf

dji = yf.download("^GSPC", period="1y", interval="1d")
print(dji)