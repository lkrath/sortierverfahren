# eine rekursive Funktion, welche die nte Fibonacci-Zahl ausgibt
import time

fib_cache = {}

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mit_cache(n):
    if n in fib_cache:
        return fib_cache[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        value = fib(n-1) + fib(n-2)
        fib_cache[n] = value
        return value

before = time.time()
print(fib(30))
after = time.time()

print(after - before)

before = time.time()
fib(30)
after = time.time()

print(after - before)