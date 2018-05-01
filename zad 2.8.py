tekst = input("Podaj tekst: ")
licznik = 0
pomiedzy_nawiasami = False


for lit in tekst:
    if lit == '>':
        pomiedzy_nawiasami = False
    if pomiedzy_nawiasami:
        licznik += 1
    if lit == '<':
        pomiedzy_nawiasami = True




print(licznik)