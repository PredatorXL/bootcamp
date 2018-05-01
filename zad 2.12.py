lista = [31,135,45,-31,-13213,512,43,24231]

for podstawiony_indeks in range(len(lista) - 1):
    min_indeks = podstawiony_indeks

    for kandydat_na_wartosc_min in range(podstawiony_indeks + 1, len(lista)):
        if lista[kandydat_na_wartosc_min] < lista[min_indeks]:
            min_indeks = kandydat_na_wartosc_min
    lista[podstawiony_indeks], lista[min_indeks] = lista[min_indeks], lista[podstawiony_indeks]

print(lista)