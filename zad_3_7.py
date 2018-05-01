def przytnij(data, start, stop):

    data = sorted(data)
    wynik = []
    czy_dodawaj = False

    for element in data:
        if start(element):
            czy_dodawaj = True
        if czy_dodawaj:
            wynik.append(element)
        if stop(element):
            break

    return wynik




def test_przycięcie():
    assert przytnij(data=[1, 2, 3, 4, 5, 6, 7], start=lambda x: x > 3, stop=lambda x: x == 6) == [4, 5, 6]
    assert przytnij(data=[1, 2, 3, 4], start=lambda x: x >= 1, stop=lambda x: x == 4) == [1, 2, 3, 4]
    assert przytnij(data=[1, 2, 3, 4, 5, 6, 7], start=lambda x: x == 3, stop=lambda x: x == 6) == [3, 4, 5, 6]

def test_funkcja_lub_lambda():
    def definicja_start(x):
        return x > 3

    wynik = przytnij(data=[1, 2, 3, 4, 5, 6, 7],
                     start=definicja_start,
                     stop=lambda x: x == 6)

    assert wynik == [4, 5, 6]

