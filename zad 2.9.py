slownik = {'Mięso': 100, 'Jabłko': 20, 'Jajko': 30}

for nazwa in slownik:
    print(f"{nazwa}: {slownik[nazwa]}/kg")

produkt = input("podaj nazwę produktu: ")
waga = float(input("podaj wagę: "))

cena = waga * slownik[produkt]
print(f"Do zapłaty {cena} PLN")
