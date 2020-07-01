# Türme von Hanoi

# Anzahl Scheiben        Anzahl Züge
#   1                       1
#   2                       3
#   3                       7
#   4                       15
#   5                       31

# für jede zusätzliche Scheibe 2x so viele Züge + 1

i = 1
az = 0

def toh(n):
    if i <= n:
        