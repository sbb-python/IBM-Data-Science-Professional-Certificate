import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
table_rows = table.find_all('tr')
table_data = []
for row in table_rows:
    cells = row.find_all(['th', 'td'])
    row_data = [cell.get_text(strip=True) for cell in cells]
    table_data.append(row_data)
# Filter out rows with empty cells
table_data = [row for row in table_data if row]
print("Table Data:")
for row in table_data:
    print(row)
try:
    tesla_revenue = pd.DataFrame(table_data[1:], columns=table_data[0])
    print("\nLast five rows of Tesla revenue data:")
    print(tesla_revenue.tail())
except Exception as e:
    pass
