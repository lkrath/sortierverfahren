import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups())

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHaHaHa')
print(mo1.group())

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo = greedyHaRegex.search('HaHaHaHaHa')
print(mo.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

xmasRegex = re.compile(r'\d+\s\w+') 
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords')
print(mo)

vowelRegex = re.compile(r'[^aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search(' Hello, world!')
print(mo)

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
print(mo)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Ina Leona Last Name: Krath')
print(mo.groups())

nongreedyRegex = re.compile(r'<.*>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

noNewlineRegex = re.compile('.*', re.DOTALL)
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)

robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoBoCop is part man, part machine, all cop.').group()
print(mo)

# Augabe 20

r = re.compile(r'\d{1,3}((,\d{3})?)*')
mo = r.search('67,338,352')
print(mo.group())

# Aufgabe 21

r = re.compile(r'[A-Z]\w+\sWatanabe')
mo = r.search('Haruto Watanabe')
print(mo.group())

# Aufgabe 22

r = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|baseballs|cats)\.', re.I)
mo = r.search('Alice eats cats.')
print(mo.group())