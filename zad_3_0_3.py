def policz_slowa(tekst):

    slownik = {}

    for slowo in tekst.split(' '):

        if slowo in slownik:
            slownik[slowo] += 1
        else:
            slownik[slowo] = 1

    return slownik


# def test_pusty_string():
#     assert policz_slowa("") ==

def test_wyrazenie():
    assert policz_slowa('Ala ma kota i kot ma Ale') == {'Ala': 1, 'ma': 2, 'kota': 1, 'i': 1, 'kot': 1, 'Ale': 1}