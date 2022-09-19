import random

r = 0
sum = 0

while True:
    r = random.randint(0,30)
    sum += r
    if r == 15 or r == 25:
        break

print(sum)