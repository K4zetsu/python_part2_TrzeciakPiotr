wiek = int(input("Podaj swój wiek kandydacie: "))

kategoria = input("Czy masz kategorię A2? tak/nie: ")

if kategoria == "tak" or kategoria == "Tak":
    okres = int(input("jak długo masz kategorią A2? w latach: "))

wynik = True if wiek == 20 and kategoria == "tak" and okres >= 2 else False
wynik = True if wiek >= 24 else False

if wynik == True:
    print("możesz zrobić prawko")
else: print("nie możesz zrobić prawka")
