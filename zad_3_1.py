def czy_jest_pierwsza(liczba):
    jest_pierwsza = True
    limit = int(liczba/2)+1

    for n in range(2, limit):
        if liczba % n == 0:
            jest_pierwsza = False
            break

    return jest_pierwsza


# python -m pytest (nazwa pliku)

def test_czy_liczba_jest_pierwsza():
    assert czy_jest_pierwsza(3) == True
    assert czy_jest_pierwsza(31) == True
    assert czy_jest_pierwsza(97) == True

def test_czy_liczba_nie_jest_pierwsza():
    assert czy_jest_pierwsza(4) == False
    assert czy_jest_pierwsza(28) == False