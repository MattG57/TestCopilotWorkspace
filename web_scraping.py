import requests
from bs4 import BeautifulSoup

# Given URL of the web page
url = 'https://google.com'

# Fetch the web page
response = requests.get(url)
web_content = response.content

# Parse the web page
soup = BeautifulSoup(web_content, 'html.parser')

# Extract all hyperlinks
hyperlinks = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        hyperlinks.append(href)

# Save the extracted URLs to 'urls.txt' file
with open('urls.txt', 'w') as file:
    for hyperlink in hyperlinks:
        file.write(hyperlink + '\n')
