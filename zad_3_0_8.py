def filtruj(lista, poczatek, koniec):

    nowa = filter(lambda x: x>=poczatek and x<=koniec, lista)
    return sorted(nowa)




def test_filtruj_dane():
    lista = [-2, 10, 0, 5, 1, 16, 9]
    poczatek = 5
    koniec = 15

    wynik = [5, 9, 10]

    assert filtruj(lista, poczatek, koniec) == wynik