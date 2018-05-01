dzien = 1
suma = 0

while dzien <= 7:
    suma += int(input(f'Temperatura w {dzien} dniu tygodnia: '))
    dzien += 1

print(f'Średnia temperatura w tygodniu to {suma/7}')