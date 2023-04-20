import random

ileliczb = int(input("Podaj ilość typowanych liczb: "))
maksliczba = int(input("Podaj maksymalną losowaną liczbę: "))

liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, maksliczba)

for i in range(3):
    print("Wytypuj %s z %s liczb: " % (ileliczb, maksliczba))
    typy = set()
    i = 0
    while i < ileliczb:
        typ = int(input("Podaj liczbę %s: " % (i + 1)))
        if typ not in typy:
            typy.add(typ)
            i = i + 1

    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        print("Trafione liczby: ", trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

    print("\n" + "x" * 40 + "\n")

print("Wylosowane liczby:", liczby)