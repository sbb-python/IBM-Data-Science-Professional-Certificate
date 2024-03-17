import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# URL containing the data
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'

# Read HTML content and extract tables
tables = pd.read_html(url)

# Assuming the gme revenue dataframe is the second one extracted
gme_revenue_df = tables[1]  # Selecting the second table

gme_revenue_df.columns = ['Date', 'Revenue']

# Remove any rows with missing values
gme_revenue_df.dropna(inplace=True)

gme_revenue_df['Date'] = pd.to_datetime(gme_revenue_df['Date'])

GME = yf.Ticker("GME")
GME_data = GME.history(period="max")

GME_data.index = GME_data.index.tz_convert('America/New_York')

gme_revenue_df['Date'] = gme_revenue_df['Date'].dt.tz_localize('America/New_York')

merged_data = pd.merge(GME_data, gme_revenue_df, how='inner', on='Date')

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"))

fig.add_trace(go.Scatter(x=merged_data.index, y=merged_data['Close'], name='Share Price'), row=1, col=1)
fig.add_trace(go.Scatter(x=merged_data['Date'], y=merged_data['Revenue'], name='Revenue'), row=2, col=1)

fig.update_layout(title='Historical Share Price and Revenue for gme', xaxis_title='Date', height=600)

# Show plot
fig.show()
