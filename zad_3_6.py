def splaszcz(lista):

    wynik = []

    for i in lista:
        if isinstance(i, list):
            for zagniezdzony_element in splaszcz(i):
                wynik.append(zagniezdzony_element)
        else:
            wynik.append(i)
    return wynik

    #funkcja dla tabeli dwuwymiarowej: brak rekurencji splaszcz(i)
    #
    # for i in lista:
    #     if isinstance(i, list):
    #         for zagniezdzony_element in i:
    #             wynik.append(zagniezdzony_element)
    #     else:
    #         wynik.append(i)
    # return wynik


def test_plaszczka_pusta():
    assert splaszcz([]) == []

def test_plaszczka_plaska_lista():
    assert splaszcz([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_plaszczka():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]



