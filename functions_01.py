import random

def add(zahl1, zahl2):
    return zahl1 + zahl2

print(add(2,10))

def rand():
    return random.randint(100,200)

print(rand())

def word(arr):
    x = ''
    for i in arr:
        x += i
    return x

print(word(['H', 'a', 'l', 'l', 'o']))