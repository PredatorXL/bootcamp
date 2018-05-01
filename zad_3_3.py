def policz_znaki(napis, start='<', stop='>'):
    liczba = 0
    aktualnypoziom = 0

    for lit in napis:
        if lit == start:
            aktualnypoziom += 1
        elif lit == stop:
            aktualnypoziom -= 1
        else:
            liczba += aktualnypoziom

    return liczba


def test_przykladowe_dane():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma [kota [a kot]] ma [ale]', '[', ']')  == 18
    assert policz_znaki('a<a<a<a>>>') == 6

def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki('') == 0

def test_policz_znaki_gdy_nie_ma_nawiasow():
    assert policz_znaki('alamakotakotmaale') == 0