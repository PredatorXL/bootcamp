podstawa = input("Podaj podstawę: ")
wykładnik = input("Podaj wykładnik: ")

if podstawa.isdigit() and wykładnik.isdigit():

    podstawa = int(podstawa)
    wykładnik_liczba = int(wykładnik)

    wynik = podstawa

    while wykładnik_liczba > 1:
        wynik *= podstawa
        wykładnik_liczba -= 1

    print(f'Wynik potęgowania {podstawa} do potęgi {wykładnik} to {wynik}')

else:
    print('podane wartości muszą być liczbami')