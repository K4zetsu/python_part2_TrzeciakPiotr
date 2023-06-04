
import klasy

petla = True

while petla:
    wybor = int(input("""Wybierz figurę, której obliczymy pole i obwód
    1. Kwadrat
    2. Prostokąt
    3. Romb
    4. Równolgełobok
    5. Trójkąt
    6. Trapez
    7. KONIEC
    Wybierz numer od 1 do 6: """))

    if wybor == 1:
        a = int(input("Wpisz długość boku kwadratu: "))
        kwadrat = klasy.Kwadrat(a)
        print(f"Pole kwadratu wynosi: {kwadrat.pole()}")
        print(f"Obwód kwadratu wynosi: {kwadrat.obwod()}")
    elif wybor == 2:
        a = int(input("Wpisz długość pierwszego boku: "))
        b = int(input("Wpisz długość drugiego boku: "))
        prostokat = klasy.Prostokat(a, b)
        print(f"Pole prostokatu wynosi: {prostokat.pole()}")
        print(f"Obwód prostokatu wynosi: {prostokat.obwod()}")
    elif wybor == 3:
        a = int(input("Wpisz długość podstawy: "))
        h = int(input("Wpisz wysokość: "))
        romb = klasy.Romb(a, h)
        print(f"Pole rombu wynosi: {romb.pole()}")
        print(f"Obwód rombu wynosi: {romb.obwod()}")
    elif wybor == 4:
        a = int(input("Wpisz długość podstaw: "))
        b = int(input("Wpisz długość boków: "))
        h = int(input("Wpisz wysokość: "))
        rownoleglobok = klasy.Rowoleglobok(a, b, h)
        print(f"Pole równoległoboku wynosi: {rownoleglobok.pole()}")
        print(f"Obwód równoległoboku wynosi: {rownoleglobok.obwod()}")
    elif wybor == 5:
        a = int(input("Wpisz długość podstawy: "))
        b = int(input("Wpisz długość boku: "))
        h = int(input("Wpisz wysokość: "))
        trojkat = klasy.Trojkat(a, b, h)
        print(f"Pole trójkąta wynosi: {trojkat.pole()}")
        print(f"Obwód trójkąta wynosi: {trojkat.obwod()}")
    elif wybor == 6:
        a = int(input("Wpisz długość pierwszej podstawy a: "))
        b = int(input("Wpisz długość drugiej podstawy b: "))
        c = int(input("Wpisz długość boku: "))
        h = int(input("Wpisz wysokość: "))
        trapez = klasy.Trapez(a, b, c, h)
        print(f"Pole trapezu wynosi: {trapez.pole()}")
        print(f"Obwód trapezu wynosi: {trapez.obwod()}")
    elif wybor == 7:
        print("Dziękuję za skorzystanie!")
        petla = False
        break






