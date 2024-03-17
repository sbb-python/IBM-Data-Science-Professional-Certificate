import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table element
table = soup.find('table')

# Extract data from the table
table_rows = table.find_all('tr')

# Initialize an empty list to store table data
table_data = []

# Iterate over the table rows
for row in table_rows:
    # Find all cells in the row
    cells = row.find_all(['th', 'td'])
    
    # Extract text content from each cell and remove leading/trailing whitespace
    row_data = [cell.get_text(strip=True) for cell in cells]
    
    # Append the row data to the table data list
    table_data.append(row_data)

# Print the table data (list of lists)
for row in table_data:
    print(row)
