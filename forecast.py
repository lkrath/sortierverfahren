import requests
from bs4 import *
from bs4 import NavigableString, Tag

from app import app

page = requests.get("https://www.wetter.net/wetter/deutschland/bornheim_(rheinland)") # Seite heute

if (page.status_code == 200):
    print('downloaded successfully')

soup = BeautifulSoup(page.content, 'html.parser')

# font 
a = "<p style = \"font-family:arial,helvetica;\">"

a += "<b>Heute:</b> <br><br>"


# Temperatur heute
theute = soup.find('div', {'class': 'col-sm-6 tempMaxDiv'})

for body_child in theute.children:
    if isinstance(body_child, NavigableString):
        continue
    if isinstance(body_child, Tag):
        a += body_child.get_text() + " "

a += "<br>"

allcolsm6 = soup.find_all('p', {'class', 'right tableText'})

# Regengeschwindigkeit heute 
rheute = allcolsm6[0].get_text()
a += "Regenwahrscheinlichkeit " + rheute + "<br>"

# Windgeschwindigkeit heute
wheute = allcolsm6[1].get_text()
a += "Windgeschwindigkeit " + wheute + "<br>"

# Luftfeuchtigkeit heute
lheute = allcolsm6[2].get_text()
a += "Luftfeuchtigkeit " + lheute + "<br>"

# Sonnenstunden heute 
sheute = allcolsm6[5].get_text()
a += "Sonnenstunden " + sheute + "<br>"

a += "<br><br>"




page2 = requests.get("https://www.wetter.net/wetter/deutschland/bornheim_(rheinland)/vorhersage-fuer-morgen") # Seite morgen

soup2 = BeautifulSoup(page2.content, 'html.parser')

a += "<b>Morgen:</b> <br><br>"


# Temperatur morgen
t2 = soup2.find('div', {'class': 'col-sm-6 tempMaxDiv'})

for body_child in t2.children:
    if isinstance(body_child, NavigableString):
        continue
    if isinstance(body_child, Tag):
        a += body_child.get_text() + " "

a += "<br>"

allcolsm6 = soup2.find_all('p', {'class', 'right tableText'})

# Regengeschwindigkeit morgen 
r2 = allcolsm6[0].get_text()
a += "Regenwahrscheinlichkeit " + r2 + "<br>"

# Windgeschwindigkeit morgen
w2 = allcolsm6[1].get_text()
a += "Windgeschwindigkeit " + w2 + "<br>"

# Luftfeuchtigkeit morgen
l2 = allcolsm6[2].get_text()
a += "Luftfeuchtigkeit " + l2 + "<br>"

# Sonnenstunden morgen
s2 = allcolsm6[5].get_text()
a += "Sonnenstunden " + s2 + "<br>"

a += "<br><br>"




page3 = requests.get("https://www.wetter.net/wetter/deutschland/bornheim_(rheinland)/vorhersage-fuer-tag-3") # Seite übermorgen

soup3 = BeautifulSoup(page3.content, 'html.parser')

a += "<b>Übermorgen:</b> <br><br>"


# Temperatur übermorgen
t3 = soup3.find('div', {'class': 'col-sm-6 tempMaxDiv'})

for body_child in t3.children:
    if isinstance(body_child, NavigableString):
        continue
    if isinstance(body_child, Tag):
        a += body_child.get_text() + " "

a += "<br>"

allcolsm6 = soup3.find_all('p', {'class', 'right tableText'})

# Regengeschwindigkeit übermorgen 
r3 = allcolsm6[0].get_text()
a += "Regenwahrscheinlichkeit " + r3 + "<br>"

# Windgeschwindigkeit übermorgen
w3 = allcolsm6[1].get_text()
a += "Windgeschwindigkeit " + w3 + "<br>"

# Luftfeuchtigkeit übermorgen
l3 = allcolsm6[2].get_text()
a += "Luftfeuchtigkeit " + l3 + "<br>"

# Sonnenstunden übermorgen
s3 = allcolsm6[5].get_text()
a += "Sonnenstunden " + s3 + "<br>"

a += "</p>"

@app.route('/')
@app.route('/index')

def index():
    return a