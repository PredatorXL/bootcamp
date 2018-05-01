from random import randint     #importujemy z katalogu random funkcję randint, która posłuży do tworzenia losowych koordynatów

x_skarb = randint(1,10)
y_skarb = randint(1,10)
x_gracz = randint(1,10)
y_gracz = randint(1,10)
minimalna_liczba_kroków = abs(x_gracz - x_skarb) + abs(y_gracz - y_skarb)
liczba_krokow_w_rundzie = 0
liczba_krokow = 0
print(f"POZYCJA STARTOWA: {x_gracz}, {y_gracz}")

while True:
    #print(f"Gracz: {x_gracz}, {y_gracz}")
    #print(f"Skarb: {x_skarb}, {y_skarb}")
    odleglosc_przed = abs(x_gracz - x_skarb) + abs(y_gracz - y_skarb)               # obliczamy odleglosc. abs = wartosc bezwzgledna

    kroki = input("Podaj kierunek ruchu: ")                                        #Poruszanie się po planszy
    if kroki == "p":
        x_gracz = x_gracz + 1
        print(f"Twoja lokalizacja: {x_gracz}, {y_gracz}")
    elif kroki == "l":
        x_gracz = x_gracz - 1
        print(f"Twoja lokalizacja: {x_gracz}, {y_gracz}")
    elif kroki == "g":
        y_gracz = y_gracz + 1
        print(f"Twoja lokalizacja: {x_gracz}, {y_gracz}")
    elif kroki == "d":
        y_gracz = y_gracz - 1
        print(f"Twoja lokalizacja: {x_gracz}, {y_gracz}")
    else:
        print("podałeś złe dane wejściowe")
        continue
    liczba_krokow_w_rundzie += 1
    liczba_krokow += 1


    if x_gracz > 10 or x_gracz < 1 or y_gracz > 10 or y_gracz < 1:                  # Wypadanie poza planszę
        print("Jesteś poza planszą!")
        break

    if x_gracz == x_skarb and y_gracz == y_skarb:                                   # Znalezienie skarbu
        print(f"Znalazłeś skarb w {liczba_krokow_w_rundzie} ruchach!")
        break

    odleglosc_po = abs(x_gracz - x_skarb) + abs(y_gracz - y_skarb)

    if randint(1,5) == 1:                                                            #Gdy losowa liczba = 1, to podpowiedź się nie wyświetli
        pass
    elif odleglosc_po < odleglosc_przed:                                            # Podpowiedzi
        print("Ciepło!")
    else:
        print("Zimno!")

    if liczba_krokow >= minimalna_liczba_kroków * 2:                                # Przeniesienie skarbu w inne miejsce
        print("Skarb zostaje przeniesiony!")
        x_skarb = randint(1, 10)
        y_skarb = randint(1, 10)
        minimalna_liczba_kroków = abs(x_gracz - x_skarb) + abs(y_gracz - y_skarb)
        liczba_krokow_w_rundzie = 0
