import pandas as pd

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'

# Read HTML content and extract tables
tables = pd.read_html(url)

# Assuming the Tesla revenue dataframe is the second one extracted
tesla_revenue_df = tables[1]  # Selecting the second table

# Print the last 5 rows of the DataFrame
print(tesla_revenue_df.tail())
