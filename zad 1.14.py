maximum = None
minimum = None
while True:
    liczba = input('Podaj liczbę: ')
    if liczba == 'stop':
        break
    if liczba == '':                                    #obsługa scenariusza: naciśnięcie enter bez wpisywania liczby
        continue

    liczba_float = float(liczba)

    if maximum is None or liczba_float > maximum:
        maximum = liczba_float                          #nowa liczba maksymalna zapisuje się jako maximum
    if minimum is None or liczba_float < minimum:
        minimum = liczba_float                         #nowa liczba minimalna zapisuje się jako minimum

if maximum is None and minimum is None:
    print('Nie podałeś żadnej liczby')                #obsługa scenariusza, w którym nie podano żadnej liczby

print(f'maximum = {maximum}')
print(f'minimum = {minimum}')