def lata_przestępne(rok):

    podzielny_przez_4 = rok % 4 is 0
    niepodzielny_przez_100 = rok % 100 is not 0
    podzielny_przez_400 = rok % 400 is 0

    return (podzielny_przez_4 and niepodzielny_przez_100) or podzielny_przez_400


def zbior_lat_przestepnych(start, koniec):
    lista = []

    for rok in range(start, koniec):
        if lata_przestępne(rok):
            lista.append(rok)

    return lista



def test_czy_sa_przestepne():
    odpowiedz = [1992, 1996, 2000, 2004, 2008, 2012, 2016]
    assert zbior_lat_przestepnych(1990, 2020) == odpowiedz

def test_czy_rok_przestepny():
    assert lata_przestępne(1992)
    assert lata_przestępne(1996)

def test_czy_rok_nie_jest_przestepny():
    assert not lata_przestępne(1991)
    assert not lata_przestępne(1669)