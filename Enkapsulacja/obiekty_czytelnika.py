import czytelnik

how_many = int(input("Jak wielu czytelników chcesz dodać?"))
for i in range (0, how_many, +1):
    czytelnik_1 = czytelnik.Czytelnik(
        czytelnik_imie = "mariusz",
        czytelnik_nazwisko = "Mocny full",
        czytelnik_wiek = 23,
        numer_karty = 234576,
        adres_zamieszkania = "chmielna 19"
    )
    print(f"czytelnik: {czytelnik_1}")