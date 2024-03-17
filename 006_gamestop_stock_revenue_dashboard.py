import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
GME = yf.Ticker("GME")
GME_data = GME.history(period="1y")
print("Tesla Stock Data:")
print(GME_data.head())
revenue_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
response = requests.get(revenue_url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    revenue_table = soup.find('table')
    # Convert revenue table to DataFrame
    revenue_df = pd.read_html(io.StringIO(str(revenue_table)))[0]
    # Display revenue data
    print("\nRevenue Data:")
    print(revenue_df)
else:
    print("Failed to fetch revenue data. Status code:", response.status_code)
