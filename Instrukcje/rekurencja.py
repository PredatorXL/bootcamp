# rekurencja = funkcja, która sama się wywołuje

def przyklad(a, limit=10):
    if a is limit:
        return False

    print(a)
    return przyklad(a+1)

przyklad(1)