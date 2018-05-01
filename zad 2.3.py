lista = [1,4,463,423,-32131,-231,-321,423,5,0]
liczba_dodatnia = 0
liczba_ujemna = 0


for liczba in lista:
    if liczba > 0:
        liczba_dodatnia += 1
    elif liczba == 0:
        pass
    else:
        liczba_ujemna += 1

print(f"Ilość liczb dodatnich: {liczba_dodatnia}")
print(f"Ilość liczb ujemnych: {liczba_ujemna}")