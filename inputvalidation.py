import pyinputplus as pyip

#while True:
#    print('Enter your age:')
#    age = input()
#    try:
#        age = int(age)
#    except:
#        print('Please use numeric digits.')
#        continue
#    if age < 1:
#        print('Please enter a positive number.')
#        continue
#    break
#print(f'Your age is {age}')

#response = pyip.inputNum()
#print(response)

#response = pyip.inputInt(prompt='Enter a number: ')
#print(response)

#response = pyip.inputNum('Enter num: ', min=4)
#print(response)

#response = pyip.inputNum('Enter num: ', greaterThan=4)

#response = pyip.inputNum('> ', min=4, lessThan=6)

#response = pyip.inputNum(blank=True)

#response = pyip.inputNum(timeout=2)

#response = pyip.inputNum(limit=2, default='N/A')
#print(response)

#response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
#print(response)

#response = pyip.inputNum(blockRegexes=[r'[02468]$'])
#print(response)

#response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])

#def addsUpToTen(numbers):
#    numbersList = list(numbers)
#    for i, digit in enumerate(numbersList):
#        numbersList[i] = int(digit)
#    if sum(numbersList) != 10:
#        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
#    return int(numbers)

#response = pyip.inputCustom(addsUpToTen)

# Aufgabe 4

response = pyip.inputNum(min=0, max=99)
