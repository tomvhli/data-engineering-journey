import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the webpage
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
response = requests.get(url)
print(f"Status Code: {response.status_code}")  # Should print 200 (success)

# Step 2: Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the table (we'll use the first table on the page)
table = soup.find('table', {'class': 'wikitable'})

# Step 4: Extract table rows
rows = table.find_all('tr')

# Step 5: Loop through rows and extract data
data = []
for row in rows[1:]:  # Skip header row
    cols = row.find_all('td')
    if len(cols) >= 3:  # Ensure we have enough columns
        country = cols[0].text.strip()
        gdp = cols[1].text.strip()
        data.append([country, gdp])

# Step 6: Save to CSV
df = pd.DataFrame(data, columns=['Country', 'GDP (US$)'])
df.to_csv('countries_gdp.csv', index=False)
print("Data saved to countries_gdp.csv!")