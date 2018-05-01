miastoA = input("Podaj nazwę miasta A: ")
miastoB = input("Podaj nazwę miasta B: ")
dystans = float(input(f"Podaj dystans z {miastoA} do {miastoB}: "))
cena = float(input("Podaj cenę paliwa: "))
spalanie = float(input("Podaj średnie spalanie na 100 km: "))

print(f'''
Koszt przejazdu {miastoA}-{miastoB} to {round(cena*spalanie*dystans/100,2)} zł''')