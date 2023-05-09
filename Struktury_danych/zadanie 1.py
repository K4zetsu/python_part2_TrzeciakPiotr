krotka = (10, -3, 4, 9, 12, -6, 0)

najwieksza = krotka[0]
najmniejsza = krotka[0]

for x in krotka:
    if najwieksza > x:
        najwieksza = x
    else: pass
    if najmniejsza < x:
        najmniejsza = x
    else: pass

print("Największa liczba krotki to: ", najwieksza)
print("Najmniejsza liczba krotki to: ", najmniejsza)