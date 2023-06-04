import czytelnik

how_many = int(input("Jak wielu czytelników chcesz dodać?"))
czytelnicy = []
for i in range (0, how_many, +1):
    czytelnik_1 = czytelnik.Czytelnik(
        czytelnik_imie = "mariusz",
        czytelnik_nazwisko = "Mocny full",
        czytelnik_wiek = 23,
        numer_karty = 234576,
        adres_zamieszkania = "chmielna 19"
    )
    czytelnicy.append(czytelnik_1)

for czytelnik_2 in czytelnicy:
    print(f"""Imię: {czytelnik_2[0]}
          Nazwisko: {czytelnik_2[1]}
          Wiek: {czytelnik_2[2]}
          Numer Karty: {czytelnik_2[3]}
          Adres: {czytelnik_2[4]}""")