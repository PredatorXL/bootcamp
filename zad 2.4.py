lista = []
ilość_liczb = 0
for liczba in range(101):
    if liczba % 3 == 0 or liczba % 5 == 0:
        ilość_liczb += 1
        lista.append(int(liczba))



print(f"Wszystkie liczby podzielne przez 3 i 5: {lista}")
print(f"Ilość liczb podzielnych przez 3 i 5: {ilość_liczb}")
