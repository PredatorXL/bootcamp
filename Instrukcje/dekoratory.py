def w_euro(funkcja):
    # ta funkcja będzie okalała oryginalną funkcję
    def dekorator(*args, **kwargs):
        return str(funkcja(*args, **kwargs) * 3.5) + " EURO"
    return dekorator

def podatek(funkcja):
    # ta funkcja będzie okalała oryginalną funkcję
    def dekorator(*args, **kwargs):
        return funkcja(*args, **kwargs) * 0.81
    return dekorator

def premia(funkcja):
    # ta funkcja będzie okalała oryginalną funkcję
    def dekorator(*args, **kwargs):
        return funkcja(*args, **kwargs) * 1.1
    return dekorator


# to samo co premia(podatek(zwroc_wynagrodzenie))
@premia
@podatek  #dekorator
def zwroc_wynagrodzenie(ilosc_h, stawka):
    return ilosc_h * stawka

@podatek
def bez_premii(ilosc_h, stawka):
    return ilosc_h * stawka

@w_euro
@premia
@podatek
def euro(ilosc_h, stawka):
    return ilosc_h * stawka

print(f'Moje wynagrodzenie wynosi {float(zwroc_wynagrodzenie(8, 1000))}')
print(f'a bez premii {float(bez_premii(8, 1000))}')
print(f'EUROSY {euro(8, 1000)}')