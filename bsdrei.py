import requests
from bs4 import BeautifulSoup

from app import app

page = requests.get("https://weather.com/de-DE/wetter/heute/l/58f6e7daa27a17c55b080b60435aeabaccbfe4547a89e4f0ab77fbb603c38986")

if (page.status_code == 200):
    print('downloaded successfully')

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

t1 = soup.find('div', {'class': 'CurrentConditions--primary--2DOqs'})

a = "Wetter in Bornheim: \nHeute: \n"

temperatur = list(t1.children)[0]
wolken = list(t1.children)[1]
a += temperatur.get_text() + "\n"
a += wolken.get_text() + "\n"

r1 = soup.find('div', {'class': 'CurrentConditions--primary--2DOqs'})

regen = list(r1.children)[0]
a += regen.get_text()

page2 = requests.get("https://weather.com/de-DE/wetter/10tage/l/58f6e7daa27a17c55b080b60435aeabaccbfe4547a89e4f0ab77fbb603c38986#detailIndex5")

soup2 = BeautifulSoup(page2.content, 'html.parser')



a += "\nHeute Nacht: \n"

t2 = soup2.find('div', {'class': 'DailyContent--DailyContent--rTQY_'})

temp2 = list(t2.children)[0]
a += temp2.get_text() + " Höchsttemperatur \n"

r2 = soup2.find('div', {'class': 'DailyContent--value--3Xvjn'})

#regen2 = list(r2.children)[0]
#a += regen2.get_text() + " Regenwahrscheinlichkeit"


@app.route('/')
@app.route('/index')

def index():
    return a