import random
user = 0
computer = 0 
while True:
    
    x = input()
    if x == '0' : break
    elif x == 'o': x = "orzeł"
    elif x == 'r': x = "reszka"
    else:
        print("Proszę dokonać prawidłowego wyboru:")
        print("o - orzeł")
        print("r - reszka")
        print("0 - zakończenie gry")
        continue

    y = random.choice(["orzeł", "reszka"])
   
    print ("Wynik rzutu: ", y)
    
    if x == y: 
        user+=1
    else:
        computer+=1
        
    print ("Wyniki łacznie.")
    print ("Użytkownik: ", user)
    print ("Komputer: ", computer)