def formatuj(*wyrazenia, **parametry):

    tekst = '\n'.join(wyrazenia)
    for indeks in parametry:
        nazwa = '$' + indeks
        tekst = tekst.replace(nazwa, str(parametry[indeks]))
    return tekst




def test_tylko_wyrazenia():
    assert formatuj('ala', 'ma') == 'ala\nma'
    assert formatuj('ala') == 'ala'
    assert formatuj('ala', 'ma', 'kota') == 'ala\nma\nkota'

def test_tylko_jedno_podstawienie():
    assert formatuj('Mam na imie $imie', imie='Ala') == 'Mam na imie Ala'
    assert formatuj('Mieszkam w $miasto', miasto='Wrocławiu') == 'Mieszkam w Wrocławiu'

def test_formatowanie():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'