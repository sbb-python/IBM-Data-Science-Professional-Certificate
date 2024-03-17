import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data=None):
    # Plot stock prices
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data.index, stock_data['Close'], label='GameStop (GME)')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.title('GameStop Stock Prices')  # Provide a title for the graph
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot revenue data if available
    if revenue_data:
        plt.figure(figsize=(8, 5))
        plt.bar(revenue_data.keys(), revenue_data.values(), color='blue')
        plt.xlabel('Quarter')
        plt.ylabel('Revenue (USD)')
        plt.title('GameStop Revenue')
        plt.grid(axis='y')
        plt.show()
    else:
        print("Revenue data not available.")

# Fetch historical stock data for GameStop (GME)
gme = yf.Ticker("GME")
gme_data = gme.history(period="1y")

# Use make_graph function to plot GameStop stock data
make_graph(gme_data)
