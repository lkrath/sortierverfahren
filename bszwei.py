import requests
from bs4 import BeautifulSoup

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")

if (page.status_code == 200):
    print('downloaded successfully')

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
print("\n")
print(list(soup.children))
print("\n")
print([type(item) for item in list(soup.children)])
print("\n")

html = list(soup.children)[2]
print(html)
print("\n")

body = list(html.children)[3]
print(body)
print("\n")

p = list(body.children)[1]
print(p.get_text())
print("\n")

print(soup.find_all('p'))