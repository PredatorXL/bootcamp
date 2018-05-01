wysokosc = float(input('Podaj wysokość w cm: '))
szerokosc = float(input('Podaj szerokość w cm: '))
dlugosc = float(input('Podaj długość w cm: '))

print(f'''
Czy objętość większa od 1l? {(wysokosc * szerokosc * dlugosc) > 1000}''')