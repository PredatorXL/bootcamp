

def wiecej_niz(tekst, ograniczenie):

    wynik = set()
    slownik = {}


    # for i in tekst.lower():
    #     if i in slownik:
    #         slownik[i] += 1
    #     else:
    #         slownik[i] = 1
    #
    # for indeks in slownik:
    #     if slownik[indeks] > ograniczenie:
    #         wynik.add(indeks)

    for litera in tekst.lower():
        if tekst.lower().count(litera) > ograniczenie:
            wynik.add(litera)

    return wynik

def test_wystepuje_wiecej_niz_3_razy():
    assert wiecej_niz('ala ma kota', 3) == {'a'}
    assert wiecej_niz('ala ma kota ', 2) == {'a', ' '}

def test_nie_wystepuje_wiecej_razy():
    assert wiecej_niz('', 2) == set()
    assert wiecej_niz('aabbcd', 2) == set()

def test_wielkie_male_litery():
    assert wiecej_niz('AAaaaAA', 2) == {'a'}