import re

regexp = '^[a-z0-9_.-]+@[a-z0-9_.-]+\.\w{2,4}$'

def sprawdz_email(dane):
    poprawne = []
    for element in dane:
        if re.match(regexp, element):
            poprawne.append(element)

    return poprawne


def test_czy_poprawny():
    regexp = '^[a-z0-9_.-]+@[a-z0-9_.-]+\.\w{2,4}$'
    maile = [
        'test@test.pl',
        'Alamakota',
        'inny@firma.pl',
        'dupa@dupadupa.pl',
    ]


    poprawne = [
        'test@test.pl',
        'inny@firma.pl',
        'dupa@dupadupa.pl',
    ]
    assert list(filter(lambda mail: re.match(regexp, mail), maile)) == poprawne