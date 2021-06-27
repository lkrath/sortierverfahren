import requests
from bs4 import *
from bs4 import NavigableString, Tag

from app import app

page = requests.get("https://www.wetter.net/wetter/deutschland/bornheim_(rheinland)")

if (page.status_code == 200):
    print('downloaded successfully')

soup = BeautifulSoup(page.content, 'html.parser')

a = "Heute: "

theute = soup.find('div', {'class': 'col-sm-6 tempMaxDiv'})

#print(theute.prettify())

#temperatur = list(theute.children)[0]
#print(temperatur)
#a += temperatur.get_text() + " "

for body_child in theute.children:
    if isinstance(body_child, NavigableString):
        continue
    if isinstance(body_child, Tag):
        a += body_child.get_text() + " "

rheute = soup.find('div', {'class', 'col-xs-4'})

#regen = list(rheute.children)[0]
#a += "Regenwahrscheinlichkeit: " + regen.get_text() + " "

for body_child in rheute.children:
    if isinstance(body_child, NavigableString):
        continue
    if isinstance(body_child, Tag):
        a +="Regenwahrscheinlichkeit: " + body_child.get_text() + " "

@app.route('/')
@app.route('/index')

def index():
    return a