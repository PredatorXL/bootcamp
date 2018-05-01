separator = input('Podaj separator: ')
lista = []

while True:
    wyraz = input('Podaj wyraz lub „STOP”: ')
    if wyraz == "STOP":
        break
    lista.append(wyraz)

    ciag = separator.join(lista)

print(f'Twoja lista to: {ciag}')