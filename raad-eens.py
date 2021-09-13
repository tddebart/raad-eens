import random

print("Welkom bij het raad spel")
score = 0
for x in range(20):
    if x != 0 and x != 19:
        nogEens = input("Wil je nog eens raden (Y/N) ").lower()
        if nogEens == "n":
            print("Ok vaarwel")
            exit()
    print("Ronde " + str(x+1))
    rndNumber = random.randint(1,10)
    for y in range(10):
        print("")
        print("Poging " + str(y+1))
        raade = int(input("Wat denk je dat het getal is? Of als je wilt stoppen type -1 "))
        if raade == -1:
            exit()
        print("Je hebt {} geraden".format(raade))
        if raade == rndNumber:
            print("Hoera je hebt het geraden, +1 score")
            score += 1
            break

        if abs(raade - rndNumber) <= 20:
            print("Je bent heel warm")
        elif abs(raade - rndNumber) <= 50:
            print("Je bent warm")

        if raade > rndNumber:
            print("Lager")
        if raade < rndNumber:
            print("Hoger")

        if y == 9:
            print("Je hebt het helaas niet geraden volgende ronde")
    print("")
    print("Score is " + str(score))
