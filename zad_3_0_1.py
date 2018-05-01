def czy_palindrom(string):

    uproszczone = uprosc_tekst(string)
    test = ''.join(reversed(uproszczone))
    return uproszczone == test


def uprosc_tekst(string):
    return string.lower().replace(" ", "")


def test_palindrom_rozna_litera():
    assert czy_palindrom('KaJaK')

def test_palindrom_ze_spacjami():
    assert czy_palindrom('Devil lived')
    assert czy_palindrom('Was it a cat I saw')
    # nie musimy dawać ==, funkcja zwraca true

def test_czy_nie_palindrom():
    assert not czy_palindrom('Dupa')

def test_czy_dobrze_upraszcza():
    assert uprosc_tekst('KaJAK') == 'kajak'
    # sprawdzamy, czy dobrze działa funkcja 'uprosc_tekst'