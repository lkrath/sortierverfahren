import shutil, os
from pathlib import Path
import send2trash
import zipfile

p = Path.home()/'organizing_files'

shutil.copy(p/'spam.txt', p/'some_folder')
shutil.copy(p/'eggs.txt', p/'some_folder/eggs2.txt')

#shutil.copytree(p/'spam', p/'spam_backup')

print(p)
#shutil.move('/home/leona/organizing_files/bacon.txt', '/home/leona/organizing_files/eggs')
#shutil.move(p/'bacon.txt', p/'eggs/new_bacon.txt')

for filename in Path.home().glob('*.rxt'):
    #os.unlink(filename)
    print(filename)

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

for folderName, subfolders, filenames in os.walk('/home/leona/organizing_files'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')

exampleZip = zipfile.ZipFile(p/'example.zip')
print(exampleZip.namelist())
#spamInfo = exampleZip.getinfo('spam.txt')
#print(spamInfo.file_size)
#print(spamInfo.compress_size)
#print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller')

exampleZip.extractall()
exampleZip.close()

#exampleZip.extract('spam.txt')

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()