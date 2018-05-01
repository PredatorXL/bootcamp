import re

test = '81-1'
regexp = '^[0-9]{2}-[0-9]{3}$'
kody = [
    '81-154',
    '00-990',
    '45-456',
    'aaaa'
]

def sprawdz_kody(kody):
    poprawne = []
    for element in kody:
        if re.match(regexp, element):
            poprawne.append(element)

    return poprawne


def test_poprawne_kody():
    poprawne = ['81-154', '00-990', '45-456']
    assert sprawdz_kody(kody) == poprawne

def test_sprawdz_kody_lambda():
    regexp = '^[0-9]{2}-[0-9]{3}$'
    poprawne = ['81-154', '00-990', '45-456']

    tester = lambda kod: re.match(regexp, kod)
    przefiltrowane = list(filter(tester, kody))

    assert przefiltrowane == poprawne