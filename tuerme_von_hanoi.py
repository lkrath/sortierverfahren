# Türme von Hanoi

# Anzahl Scheiben        Anzahl Züge
#   1                       1
#   2                       3
#   3                       7
#   4                       15
#   5                       31

# für jede zusätzliche Scheibe 2x so viele Züge plus einen

toh_cache = {}

def toh(n):
    if n in toh_cache:
        return toh_cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        value = toh(n-1) + toh(n-1) + 1
        toh_cache[n] = value
        return value

print(toh(100))

jahre = toh(100) // 60 // 60 // 24 // 356

print('Wenn die Mönche ständig Scheiben umlegen bräuchten sie ' + str(jahre) + ' Jahre.')

        
        