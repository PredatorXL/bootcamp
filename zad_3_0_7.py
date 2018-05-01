from functools import reduce

# lista = [100, 200, 300, 400]
# wynik = reduce(lambda x,y: x+y, lista)
#
# print(wynik)

wynagrodzenie = [200, 300, 400]
cena_obiadu = 15
po_odjeciu_obiadu = map(lambda x: x-cena_obiadu, wynagrodzenie)
suma = reduce(lambda x,y: x+y, po_odjeciu_obiadu) * 0.81
print(f"Suma wynagrodzenia to: {round(suma,2)}")
