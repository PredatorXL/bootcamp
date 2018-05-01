slownik = {}

tekst = input("Wpisz tekst: ")

for lit in tekst:
    if lit in slownik:
        slownik[lit] += 1
    else:
        slownik[lit] = 1


print(tekst)
print(slownik)
