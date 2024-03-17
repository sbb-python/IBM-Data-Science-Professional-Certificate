import yfinance as yf

# Create a Ticker object for GameStop (GME)
gme = yf.Ticker("GME")

# Fetch historical market data for GameStop stock
gme_data = gme.history(period="1y")

# Display the downloaded data
print(gme_data.head())
