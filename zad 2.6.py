lista = [31,135,45,-31,-13213,512,43,24231]
maximum = 0
minimum = 0

for i in range(1, len(lista)):
    if lista[i] < lista[minimum]:
        minimum = i
    if lista[i] > lista[maximum]:
        maximum = i

lista[minimum], lista[maximum] = lista[maximum], lista[minimum]

print(lista)
