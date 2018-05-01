pierwsza = float(input('Podaj pierwszą liczbę: '))
druga = float(input('Podaj drugą liczbę: '))
rodzaj = input('Podaj rodzaj operacji: ')

if rodzaj == '+':
    print(f'Wynik: {pierwsza + druga}')
elif rodzaj == '-':
    print(f'Wynik: {pierwsza - druga}')
elif rodzaj == '*':
    print(f'Wynik: {pierwsza * druga}')
if rodzaj == '/':
    print(f'Wynik: {pierwsza / druga}')     # w tym wypadku można użyć zarówno if jak i elif, logicznie wychodzi na to samo
else:
    print('złe dane')