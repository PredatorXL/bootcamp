def podwojenie(liczba):
    return liczba * 2

def pomniejszenie(liczba):
    return liczba / 2

def zwieksz(liczba, operacja):
    return operacja(liczba) + 1


# zwieksz_lambda = lambda liczba: liczba + 1
# print(zwieksz(1))
# print(zwieksz_lambda(2))

wynik = zwieksz(100, podwojenie)
wynik2 = zwieksz(100, pomniejszenie)
wynik3 = zwieksz(100, lambda x: x * 1.23) # x to argument lokalny, który dotyczy tylko i wylącznie lambdy

print(wynik)
print(wynik2)
print(wynik3)