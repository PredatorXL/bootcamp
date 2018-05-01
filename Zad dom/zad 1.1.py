lista = [4, -3, 100, 0, -4, 2]
wynik = 1

for i in lista:
    wynik = wynik * (i > 0 and i or - i) or 1

print(wynik)