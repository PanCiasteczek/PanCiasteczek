import sys
import random
import time

gramy = (input("Cześć, zagramy w papier kamień nożyce? (y/n):\n"))
if gramy.lower() == "n":
    print("Trudno...")
    sys.exit(0)

print("(Jeśli zechcesz zakończyć grę wpisz '10'.)")
time.sleep(0.5)
while True:
    print()

    wybor = int(input("Wybierasz:\n1.Papier\n2.Kamień\n3.Nożyce\n"))
    wybor_komp = random.randrange(1, 3)

    if wybor == 10:
        sys.exit(0)

    print("3..")
    time.sleep(0.5)
    print("2..")
    time.sleep(0.5)
    print("1..")
    time.sleep(0.5)

    if wybor == 1 and wybor_komp == 1:
        print("Papier vs Papier")
        time.sleep(0.5)
        print("Remis!")
    elif wybor == 2 and wybor_komp == 2:
        print("Kamień vs Kamień")
        time.sleep(0.5)
        print("Remis!")
    elif wybor == 3 and wybor_komp == 3:
        print("Nożyce vs Nożyce")
        time.sleep(0.5)
        print("Remis!")

    if wybor == 1 and wybor_komp == 2:
        print("Papier vs Kamień")
        time.sleep(0.5)
        print("Wygrywasz!")
    elif wybor == 2 and wybor_komp == 3:
        print("Kamień vs Nożyce")
        time.sleep(0.5)
        print("Wygrywasz!")
    elif wybor == 3 and wybor_komp == 1:
        print("Nożyce vs Papier")
        time.sleep(0.5)
        print("Wygrywasz!")

    if wybor == 1 and wybor_komp == 3:
        print("Papier vs Nożyce")
        time.sleep(0.5)
        print("Przegrywasz!")
    elif wybor == 2 and wybor_komp == 1:
        print("Kamień vs Papier")
        time.sleep(0.5)
        print("Przegrywasz!")
    elif wybor == 3 and wybor_komp == 2:
        print("Nożyce vs Kamień")
        time.sleep(0.5)
        print("Przegrywasz!")

    print()
    input("Wciśnij dowolny przycisk żeby grać dalej")

    import os, random, time

intro = """
Witaj w grze papier-nozyce-kamien.
1 - Papier
2 - Nozyce
3 - Kamien
0 - Koniec gry
"""

possible_moves = {1: "Papier", 2: "Nozyce", 3: "Kamien"}

play = True

# tutaj bedziemy powtarzac petle z gra do czasu az uzytkownik wybierze 0
while play:
    # czyscimy ekran
    # to komenda dla windowsa os.system("cls")
    os.system("clear")
    print(intro)
    a = int(input("Wybierz swoj ruch (0-3):"))
    if a == 0:
        print("papa, dzieki za gre")
        # break w tym miejscu przerywa petle while
        break
    elif a > 0 and a < 4:
        your_move = a
        computer_move = random.choice((1, 2, 3))
        print("Wybrales:", possible_moves.get(your_move))
        print("Komputer wylosowal:", possible_moves.get(computer_move))
        if (your_move == computer_move):
            print("Mamy remis")
        elif (your_move == 1 and computer_move == 2) or (your_move == 2 and computer_move == 3) or (
                your_move == 3 and computer_move == 1):
            print("Komputer wygral")
        else:
            print("Wygrałes z komputerem")
    else:
        print("Przegrales - zagraj jeszcze raz.")
    # dajmy pauze na 4 sekundy zeby przeczytac wynik gry
    time.sleep(4)