import random

print("Das ist ein kleines Würfelspiel.\n Sie spielen gegen den Computer.\n Wenn ihre Augensumme nach 6x Würfeln höher ist als\ndie vom Computer haben Sie gewonnen")

while True:
    print("\nSie haben nun 6 Versuche")
    sumPlayer = 0
    sumComp = 0

    for i in range(7):
        player = random.randint(1,6)
        comp = random.randint(1,6)
        sumPlayer += player
        sumComp += comp

        print(f"Sie haben eine {player} gewürfelt und der Computer eine {comp}\n")
        input("Drücken Sie eine beliebige Taste um fortzufahren ")
        continue

    if(sumPlayer > sumComp):
        print("\nSie haben gewonnen")
    else:
        print("\nDer Computer hat gewonnen")

    wiederholung = input("Wollen Sie das Spiel wiederholen[j]? ")

    if(wiederholung != "j"):
        break
