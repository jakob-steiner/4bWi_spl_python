import random

zahl1 = random.randint(0,100)
zahl2 = random.randint(0,100)

if zahl1 < zahl2 and zahl1 < 50:
    print('Zahl 1 ist kleiner als Zahl 2 und Mini')

if zahl1 < 30 or zahl2 < 30:
    print('Eine der beiden ist kleiner als 30')

if zahl1 < 50 and zahl2 != 50:
    print('Erste Zahl klein, zweite kein 50ige')
