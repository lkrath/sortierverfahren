import requests
from bs4 import BeautifulSoup

page = requests.get("https://weather.com/de-DE/wetter/heute/l/58f6e7daa27a17c55b080b60435aeabaccbfe4547a89e4f0ab77fbb603c38986")

#if (page.status_code == 200):
    #print('downloaded successfully')

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

t1 = soup.find('div', {'class': 'CurrentConditions--primary--3xWnK'})

print("Wetter in Bornheim: \nHeute: \n")

temperatur = list(t1.children)[0]
wolken = list(t1.children)[1]
print(temperatur.get_text())
print(wolken.get_text())

r1 = soup.find('div', {'class': 'CurrentConditions--precipValue--RBVJT'})

regen = list(r1.children)[0]
print(regen.get_text())

page2 = requests.get("https://weather.com/de-DE/wetter/10tage/l/58f6e7daa27a17c55b080b60435aeabaccbfe4547a89e4f0ab77fbb603c38986#detailIndex5")

soup2 = BeautifulSoup(page2.content, 'html.parser')



print("\nHeute Nacht: \n")

t2 = soup2.find('div', {'class': 'DailyContent--ConditionSummary--2vnrT'})

temp2 = list(t2.children)[0]
print(temp2.get_text() + " Höchsttemperatur")

r2 = soup2.find('div', {'class': 'DailyContent--label--3rOJ4'})

regen2 = list(r2.children)[1]
print(regen2.get_text() + " Regenwahrscheinlichkeit")



#print("\nÜbermorgen: \n")

#t3 = soup2.find('div', {'class': 'DailyContent--ConditionSummary--2vnrT'})

#temp3 = list(t3.children)[0]
#print(temp3.get_text() + " Höchsttemperatur")

#r3 = soup2.find('div', {'class': 'DailyContent--label--3rOJ4'})

#regen3 = list(r3.children)[1]
#print(regen3.get_text() + " Regenwahrscheinlichkeit")