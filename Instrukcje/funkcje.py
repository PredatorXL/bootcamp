# DRY - don't repeat yourself
#

def witaj(rejon='łazarskim'):
    print(f'Na {rejon} rejonie nie jest kolorowo')

# witaj('szczepińskim')
# witaj()

def prostokat_pole(bok1, bok2):
    pole = bok1 * bok2
    print(f"pole prostokąta to {pole}")

    return pole

def trojkat_pole(podstawa, wysokość):
    return podstawa * wysokość / 2



pole1 = prostokat_pole(10, 10)
pole2 = prostokat_pole(12, 31)

if pole1 > pole2:
    print("pole 1 jest większe")
elif pole2 > pole1:
    print("pole 2 jest większe")
else:
    print("pola są równe")

trójkąt1 = trojkat_pole(wysokość=12, podstawa=21)
print(trójkąt1)