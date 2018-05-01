liczba = float(input('Liczba: '))

print(f'''
Liczba spełnia warunek? {liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10 or liczba == 7}''')