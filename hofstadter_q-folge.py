# Hofstadter Q-Folge

hof_cache = {}

def hof(n):
    if n in hof_cache:
        return hof_cache[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        value = hof(n - hof(n-1)) + hof(n - hof(n-2))
        hof_cache[n] = value
        return value

print(hof(5))