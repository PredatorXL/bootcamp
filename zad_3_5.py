def silnia(liczba):
    if liczba == 0:
        return 1

    else:
        return liczba * silnia(liczba - 1)


def test_wynik_zero():
    assert silnia(0) == 1

def test_wynik_silni():
    assert silnia(5) == 120
    assert silnia(3) == 6
    assert silnia(1) == 1