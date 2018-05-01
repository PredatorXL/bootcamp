zbior = set()
zbior_parzyste = set(range(0,101,2))

while True:
    liczba = input("podaj liczbę: ")
    if liczba == 'stop':
        break
    zbior.add(int(liczba))

print(f"Wprowadziłeś {len(zbior)} unikalnych liczb")

wprowadzone_parzyste = zbior & zbior_parzyste

print(f"{len(wprowadzone_parzyste)} liczby parzyste")

