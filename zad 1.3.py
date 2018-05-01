Imie = 'Jan'
Wzrost = 180   # duże i małe litery mają znaczenie

print('Imię: ' + Imie)
print('Wzrost: ' + str(Wzrost))   # wzrost trzeba zamienić na str


print(f'Imię: {Imie}')       # wprowadzenie f przed ' powoduje, że możemy korzystać z funkcji mimo, że znajduje się w ''. Funkcję wprowadza się w znakach klamrowych {}

print(f'Imię: {Imie}\nWzrost: {Wzrost}')  # \n przerzuca do drugiej linii


print('Imię: ' + Imie + '\n' 'Wzrost: ' + str(Wzrost))

print('''DUPA
dupa
dupa''')                        # użycie ''' pozwala na wpisywanie tekstu w kilku linijkach