import yfinance as yf

# Create a Ticker object for Tesla (TSLA)
tsla = yf.Ticker("GME")

# Fetch historical market data for Tesla stock
tsla_data = tsla.history(period="max")

# Display the downloaded data
print(tsla_data.head())





