import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data=None):
    # Plot stock prices
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data.index, stock_data['Close'], label='Tesla (TSLA)')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.title('Tesla Stock Prices')  # Provide a title for the graph
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot revenue data if available
    if revenue_data:
        plt.figure(figsize=(8, 5))
        plt.bar(revenue_data.keys(), revenue_data.values(), color='blue')
        plt.xlabel('Quarter')
        plt.ylabel('Revenue (USD)')
        plt.title('Tesla Revenue')
        plt.grid(axis='y')
        plt.show()
    else:
        print("Revenue data not available.")

# Fetch historical stock data for Tesla (TSLA)
tsla = yf.Ticker("TSLA")
tsla_data = tsla.history(period="1y")

# Use make_graph function to plot Tesla stock data
make_graph(tsla_data)
