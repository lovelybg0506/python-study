import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/news/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup)

articles = soup.select('h3.Mb(5px)')

for article in articles:
    title = article.text.strip()
    link = article.a['href']
    print(title)
    print(link)
