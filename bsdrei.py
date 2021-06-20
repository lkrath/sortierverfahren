import requests
from bs4 import BeautifulSoup

from app import app

page = requests.get("https://www.wetter.de/deutschland/wetter-bornheim-18220759.html")

if (page.status_code == 200):
    print('downloaded successfully')

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

tempheute = soup.find('div', {'class': 'weather-daybox-base__minMax__max'})

a = "Wetter in Bornheim: \nHeute: \n "

temperatur = list(tempheute.children)[0]
a += temperatur.get_text() + "\n "

regenheute = soup.find('div', {'class': 'weather-rainindicator__chance'})

regen = list(regenheute.children)[0]
a += regen.get_text()

windheute = soup.find('div', {'class', 'weather-windindicator__description'})

wind = list(windheute.children)[0]
a += wind.get_text() + "\n "

#page2 = requests.get("https://weather.com/de-DE/wetter/10tage/l/58f6e7daa27a17c55b080b60435aeabaccbfe4547a89e4f0ab77fbb603c38986#detailIndex5")

#soup2 = BeautifulSoup(page2.content, 'html.parser')



#a += "\nHeute Nacht: \n"

#t2 = soup2.find('div', {'class': 'DailyContent--DailyContent--rTQY_'})

#temp2 = list(t2.children)[0]
#a += temp2.get_text() + " Höchsttemperatur \n"

#r2 = soup2.find('div', {'class': 'DailyContent--value--3Xvjn'})

#regen2 = list(r2.children)[0]
#a += regen2.get_text() + " Regenwahrscheinlichkeit"


@app.route('/')
@app.route('/index')

def index():
    return a