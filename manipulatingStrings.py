# in and not
print('Hello' in 'HEllo, World')
print('cats' not in 'cats and dogs')

# Strings in otehr Strings
name = 'leona'
age = 420
print('hello, my name is %s. i am %s years old.' % (name, age))
print(f'My name is {name}. Next year I will be {age + 1}.')

# Useful String Methods
spam = 'Hello, World!'
print(spam.upper())
print(spam.lower())

#print('How are you?')
#feeling = input()
#if feeling.lower() == 'great':
#    print('I feel great too')
#else:
#    print('i hope the rest of your day is good.')

print(spam.islower())
print('HELLO'.isupper())

print('hello'.isalpha())
print('hello213'.isalnum())
print('137'.isdecimal())
print('   '.isspace())
print('This is Title case'.istitle())

#while True:
#    print('Select a password (letters and numbers only)')
#    password = input()
#    if password.isalnum():
#        break
#    print('Password can only have letters and numbers')

print('Hsjadl hdo'.endswith('hdo'))
print('jska dapi'.startswith('jska'))

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'pefnpojwd']))
print('My name is iofejo'.split())
print('MyABCnameABCisABCfmoefes'.split('ABC'))

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment"
Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

print(ord('A'))
print(ord('a'))
print(chr(324))