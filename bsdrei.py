import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.dwd.de/DE/wetter/wetterundklima_vorort/nordrhein-westfalen/koeln_bonn/_node.html")

if (page.status_code == 200):
    print('downloaded successfully')

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

