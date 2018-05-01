s = "Tomek nie mówił zbyt wiele, co się z nim działo w więzieniu, żeby nas nie martwić, ale wiemy, że go maltretowali. Z tego powodu dwa razy próbował się zabić – opowiada Wirtualnej Polsce Gerard Komenda, brat Tomasza. Według byłych funkcjonariuszy jako skazany za pedofilię przeszedł piekło. - Teraz w więzieniach trwa sprawdzanie dokumentów, co się dokładnie działo za murami i w celach – słyszymy od informatora."
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
ilosc_samoglosek = 0

for lit in s:
    if lit in samogloski:
        ilosc_samoglosek += 1

print(ilosc_samoglosek)