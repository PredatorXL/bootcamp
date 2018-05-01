pierwsza = 0
druga = 1
i = 1
ilosc = int(input("Ile liczb chcesz wyświetlić?: "))

while i <= ilosc:
        pomocnicza = pierwsza

        pierwsza = druga
        druga = pomocnicza + pierwsza

        print(pierwsza, end=', ')
        i += 1
