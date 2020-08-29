# Damenproblem

n = 4
anzahl_damen = 0

# leer = 0
# bedroht > 0
# dame = -1

brett = [[0 for i in range(n)] for j in range(n)]

def setze_dame(x, y, anzahl_damen):
    if brett[x][y] > 0:
        return False
    else:
        brett[x][y] -= 1
        setze_bedrohung(x, y)
        anzahl_damen += 1
        return True

def setze_bedrohung(x, y):
    for i in range(n):
        if brett[x][i] == 0:        # waagerecht
            brett[x][i] += 1
        if brett[i][y] == 0:        # senkrecht
            brett[i][y] += 1
        if x + i < n and y + i < n:
            if brett[x+i][y+i] == 0:    # diagonal rechts oben
                brett[x+i][y+i] += 1
        if x - i >= 0 and y + i < n:
            if brett[x-i][y+i] == 0:    # diagonal links oben
                brett[x-i][y+1] += 1
        if y - i >= 0 and x + i < n:
            if brett[x+i][y-i] == 0:    # diagonal rechts unten
                brett[x+i][y-1] += 1
        if x - i >= 0 and y - i >= 0:
            if brett[x-i][y-i] == 0:    # diagonal links unten
                brett[x-i][y-1] += 1

def entferne_dame(x, y, anzahl_damen):
    brett[x][y] == 0
    entferne_bedrohung(x, y)
    anzahl_damen += 1

def entferne_bedrohung(x, y):
    for i in range(n):
        if brett[x][i] == 0:        # waagerecht
            brett[x][i] -= 1
        if brett[i][y] == 0:        # senkrecht
            brett[i][y] -= 1
        if x + i < n and y + i < n:
            if brett[x+i][y+i] == 0:    # diagonal rechts oben
                brett[x+i][y+1] -= 1
        if x - i >= 0 and y + i < n:
            if brett[x-i][y+i] == 0:    # diagonal links oben
                brett[x-i][y+1] -= 1
        if y - i >= 0 and x + i < n:
            if brett[x+i][y-i] == 0:    # diagonal rechts unten
                brett[x+i][y-1] -= 1
        if x - i >= 0 and y - i >= 0:
            if brett[x-i][y-i] == 0:    # diagonal links unten
                brett[x-i][y-1] -= 1

def zeichne_brett():
    for i in range(n):
        for j in range(n):
            if brett[j][i] == -1:
                print("x", end="   ")
            else:
                print("o", end="   ")
        print("\n")

def loesung(reihe):
    if anzahl_damen == n:
        return True
    else:
        for i in range(n):
            if brett[i][reihe] == 0:
                setze_dame(i, reihe, anzahl_damen)
                if loesung(reihe+1):
                    return True
                else:
                    entferne_dame(i, reihe, anzahl_damen)
                    #return False

def loesung2(reihe):
    if anzahl_damen == n:
        return True
    else:
        for i in range(n):
            if brett[i][reihe] == 0:
                setze_dame(i, reihe, anzahl_damen)
                if loesung2(reihe + 1) == True:
                    return True
                else:
                    entferne_dame(i, reihe, anzahl_damen) 
                    return False

loesung2(0)
zeichne_brett()