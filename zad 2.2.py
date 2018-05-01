
lista = []


while len(lista) <= 10:
    liczba = input("Podaj liczbę: ")
    if liczba == "stop":
        break
    lista.append(float(liczba))

srednia = sum(lista) / len(lista)
print(f"Średnia to {srednia}")