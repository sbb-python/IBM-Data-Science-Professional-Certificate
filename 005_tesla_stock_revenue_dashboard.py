import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# URL containing the data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'

# Read HTML content and extract tables
tables = pd.read_html(url)

# Assuming the Tesla revenue dataframe is the second one extracted
tesla_revenue_df = tables[1]  # Selecting the second table

tesla_revenue_df.columns = ['Date', 'Revenue']

# Remove any rows with missing values
tesla_revenue_df.dropna(inplace=True)

tesla_revenue_df['Date'] = pd.to_datetime(tesla_revenue_df['Date'])

tsla = yf.Ticker("TSLA")
tsla_data = tsla.history(period="max")

tsla_data.index = tsla_data.index.tz_convert('America/New_York')

tesla_revenue_df['Date'] = tesla_revenue_df['Date'].dt.tz_localize('America/New_York')

merged_data = pd.merge(tsla_data, tesla_revenue_df, how='inner', on='Date')

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"))

fig.add_trace(go.Scatter(x=merged_data.index, y=merged_data['Close'], name='Share Price'), row=1, col=1)
fig.add_trace(go.Scatter(x=merged_data['Date'], y=merged_data['Revenue'], name='Revenue'), row=2, col=1)

fig.update_layout(title='Historical Share Price and Revenue for Tesla', xaxis_title='Date', height=600)

# Show plot
fig.show()
