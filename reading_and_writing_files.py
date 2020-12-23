from pathlib import Path
import os

print(Path('spam', 'bacon', 'eggs'))
print(str(Path('spam', 'bacon', 'eggs')))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'/Documents', filename))

print(Path('spam') / 'bacon' / 'eggs')
print(Path('spam') / Path('bacon/eggs'))
print(Path('spam') / Path('bacon', 'eggs'))

homeFolder = r'/home/leona'
subFolder = 'spam'
print(homeFolder + '/' + subFolder)
print('/'.join([homeFolder, subFolder]))

homeFolder = Path('/Documents')
subFolder = Path('spam')
print(homeFolder / subFolder)
print(str(homeFolder / subFolder))

print(Path('spam') / 'bacon' / 'eggs')

print(Path.cwd())
#os.chdir('/home/leona/Documents')
print(Path.cwd())

print(Path.home())

#os.makedirs('/home/leona/Documents/delicious/walnut/waffles')

#Path(r'/home/leona/Documents/spam').mkdir()

print(Path.cwd())
print(Path.cwd().is_absolute())
print(Path('spam/bacon/eggs').is_absolute())

print(Path('my/relative/path'))
print(Path.cwd() / Path('my/relative/path'))

print(Path.home() / Path('my/relative/path'))

print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('/home', '/'))
print(os.path.relpath('/home', '/spam/eggs'))

p = Path('/home/leona/spam.txt')
print(p)
print(p.anchor)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

print(Path.cwd())
print(Path.cwd().parents[2])

calcFilePath = '/home/leona/calc.exe'
print(os.path.basename(calcFilePath))
print(os.path.dirname(calcFilePath))
print(os.path.split(calcFilePath))

print(calcFilePath.split(os.sep))

print(os.path.getsize('/home/leona/Documents/Sortierverfahren'))
print(os.listdir('/home/leona/Documents/Sortierverfahren'))

totalsize = 0
for filename in os.listdir('/home/leona/Documents/Sortierverfahren'):
    totalsize += os.path.getsize('/home/leona/Documents/Sortierverfahren')
print(totalsize)  

p = Path('/home/leona/Documents/Sortierverfahren')
p.glob('*')
print(list(p.glob('*.py')))

print(Path('/home/leona/Documents').exists())