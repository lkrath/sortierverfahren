# Bubble Sort

zahlen = [7, 9, 12, 75, 8, 78, 3, 14]

for i in range(len(zahlen)-1):
    for j in range(0, len(zahlen)-1-i):
        if zahlen[j] > zahlen[j+1]:
            zahlen[j], zahlen[j+1] = zahlen[j+1], zahlen[j]

print(zahlen)