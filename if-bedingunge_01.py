import random

x = random.randint(0,100)

if x < 20:
    print('mini')
elif x >= 20 and x < 50:
    print('medium')
else: 
    print('large')