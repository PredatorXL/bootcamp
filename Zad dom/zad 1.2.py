dzielna = int(input('Podaj liczbę dodatnią: '))
dzielnik = int(input('Podaj dzielnik: '))

# print()
# (dzielna > 0 or print('Dzielna nie jest liczbą dodatnią!')) and (dzielnik or print('Dzielnik musi być różny od 0!')) and print(f'Wynik dzielenia to {dzielna / dzielnik}')

if dzielna <= 0:
    print('Dzielna nie jest liczbą dodatnią!')
    #break
if dzielnik == 0:
    print('Dzielnik musi być różny od 0!')
else:
    print(f'Wynik dzielenia to {dzielna / dzielnik}')