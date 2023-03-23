import random

print("Wybierz papier, kamien, nozyce")
while True:
    print()

    wybor = int(input("Wybierz:\n1.Papier\n2.Kamien\n3.Nozyce\n"))
    wybor_komp = random.randrange(1, 3)

    if wybor == 1 and wybor_komp == 1:
        print("Papier vs Papier")
        print("Remis!")
    elif wybor == 2 and wybor_komp == 2:
        print("Kamien vs Kamien")
        print("Remis!")
    elif wybor == 3 and wybor_komp == 3:
        print("Nozyce vs Nozyce")
        print("Remis!")

    if wybor == 1 and wybor_komp == 2:
        print("Papier vs Kamien")
        print("Wygrywasz!")
    elif wybor == 2 and wybor_komp == 3:
        print("Kamień vs Nozyce")
        print("Wygrywasz!")
    elif wybor == 3 and wybor_komp == 1:
        print("Nozyce vs Papier")
        print("Wygrywasz!")

    if wybor == 1 and wybor_komp == 3:
        print("Papier vs Nozyce")
        print("Przegrywasz!")
    elif wybor == 2 and wybor_komp == 1:
        print("Kamien vs Papier")
        print("Przegrywasz!")
    elif wybor == 3 and wybor_komp == 2:
        print("Nozyce vs Kamien")
        print("Przegrywasz!")

    print()
    input("Kliknij dowolny przycisk, aby grac dalej")