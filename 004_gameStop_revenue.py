import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
# Extract data from the table
table_rows = table.find_all('tr')
table_data = []
# Iterate over the table rows
for row in table_rows:
    # Find all cells in the row
    cells = row.find_all(['th', 'td'])
     # Extract text content from each cell and remove leading/trailing whitespace
    row_data = [cell.get_text(strip=True) for cell in cells]
    # Append the row data to the table data list
    table_data.append(row_data)
for row in table_data:
    print(row)
