EUR = 4.20
USD = 3.54
CHF = 3.58

operacja = input("Czy chcesz dokonać kupna, czy sprzedaży? :")
if operacja in ['k', 's']:
    waluta = input("Jaką walutę chcesz wybrać?: ")

    if operacja == 'k':
        ilosc = input("Ile zł chcesz wymienić?: ")
        if waluta == 'EUR':
            wynik = float(ilosc) / EUR
        elif waluta == 'USD':
            wynik = float(ilosc) / USD
        else:
            wynik = float(ilosc) / CHF

        komunikat = f'{ilosc} PLN to {wynik} {waluta}'
    else:
        ilosc = input(f"Ile {waluta} chcesz zakupić? :")
        if waluta == 'EUR':
            wynik = float(ilosc) * EUR
        elif waluta == 'USD':
            wynik = float(ilosc) * USD
        else:
            wynik = float(ilosc) * CHF

        komunikat = f'{ilosc} {waluta} to {wynik:.2f} PLN'

    print(komunikat)
else:
    print("błąd")



