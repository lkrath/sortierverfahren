# Selection Sort

zahlen = [7, 9, 12, 75, 8, 78, 3, 14]

for i in range(len(zahlen)):
    
    kleinste = i

    for j in range(i+1, len(zahlen)):
        if zahlen[kleinste] > zahlen[j]:
            kleinste = j
    
    zahlen[i], zahlen[kleinste] = zahlen[kleinste], zahlen[i]


print(zahlen)
