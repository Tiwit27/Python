import random
import datetime

play = True
while(play):
    liczby = []
    liczbyGracza = []
    trafione = 0
    trafioneLiczby = []
    wylosowane = []
    plik = open("zapis.txt", "a")
    czas = datetime.datetime.now()
    plik.write("Czas losowania: " + str(czas.strftime("%c")) + "\n")

    print(czas.strftime("%c"))
    for i in range(49):
        liczby.append(i + 1)

    while len(liczbyGracza) < 6:
        x = input("Wytypuj kolejną liczbę: ")
        if(int(x) in liczbyGracza):
            print("Ta liczba została już wytypowana, podaj inną")
        elif int(x) < 1 or int(x) > 49:
            print("Podałeś liczbę z poza zakresu, podaj inną")
        elif int(x) > 0 and int(x) < 50:
            liczbyGracza.append(int(x))

    def losuj():
        global trafione
        x = random.choice(liczby)
        wylosowane.append(x)
        if(int(x) in liczbyGracza):
            trafione += 1
            trafioneLiczby.append(x)
        liczby.remove(x)
        return x



    for i in range(6):
        losuj()

    print("Wylosowane liczby to: " + str(wylosowane))
    plik.write("Wylosowane liczby: " + str(wylosowane) + "\n")
    print("Liczby wytypowane: " + str(liczbyGracza))
    plik.write("Wytypowane liczby: " + str(liczbyGracza) + "\n")

    print("Trafiłeś " + str(trafione) + " liczb: " + str(trafioneLiczby))
    plik.write("Trafione Liczby: " + str(trafioneLiczby) + "\n")
    plik.write("------------------------------------------" + "\n")
    plik.close()
    c = True
    while(c):
        print("-------------------------------------")
        print("Co teraz chcesz zrobić?")
        print("1. Gramy dalej")
        print("2. Koniec gry")
        wybor = input("Wybieram: ")
        if(wybor == "1"):
            play = True
            c = False
        elif(wybor == "2"):
            play = False
            c = False




