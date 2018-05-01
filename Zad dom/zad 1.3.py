ograniczenie_dolne = 0
ograniczenie_gorne = 100
podział = int((ograniczenie_gorne - ograniczenie_dolne)/2)



while True:
    pytanie = input(f'czy twoja liczba jest większa od {podział}? ')
    if pytanie == 't':
        ograniczenie_dolne = podział
        podział = int(ograniczenie_dolne+(ograniczenie_gorne - ograniczenie_dolne)/2)
        # print(ograniczenie_dolne)
        # print(ograniczenie_gorne)
    elif pytanie == 'n':
        ograniczenie_gorne = podział
        podział = int(ograniczenie_dolne+(ograniczenie_gorne - ograniczenie_dolne) / 2)
        # print(ograniczenie_dolne)
        # print(ograniczenie_gorne)
    else:
        print("błąd")

    if ograniczenie_gorne - ograniczenie_dolne == 1:
        print(f'Twoja liczba to {ograniczenie_gorne}')
        break




