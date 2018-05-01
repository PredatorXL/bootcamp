# netto = [100, 200, 300, 400]
# brutto = map(lambda x: x * 1.23, netto)
#
# imiona = ['Janek', 'Adam', 'Ewa']
# malymi = map(lambda x: x.lower(), imiona)
#
# print(list(brutto))
# print(list(malymi))

def policz_vat(stawka_vat):

    mnoznik = stawka_vat/100 + 1
    return lambda x: round(x * mnoznik, 1)



def test_policz_vat_23():

    netto = [100, 200, 300, 400]
    brutto_23 = policz_vat(23)
    brutto = map(brutto_23, netto)
    assert list(brutto) == [123.0, 246.0, 369.0, 492.0]


def test_policz_vat_10():
    netto = [100, 200, 300, 400]
    brutto_10 = policz_vat(10)
    brutto = map(brutto_10, netto)
    assert list(brutto) == [110.0, 220.0, 330.0, 440.0]