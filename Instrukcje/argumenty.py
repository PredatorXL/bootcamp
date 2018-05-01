def example(*args, **kwargs):
    print(args)
    print(kwargs)

example(1, 2, 3, 4)
example(imie='Jan', nazwisko='Kowalski')
example(1, 2, pensja=1000)


def przyklad(**kwargs):
    for indeks in kwargs:
        print(f'{indeks}: {kwargs[indeks]}')

przyklad(imie='test', nazwisko='aa')