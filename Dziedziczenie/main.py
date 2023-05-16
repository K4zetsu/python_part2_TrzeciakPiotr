
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
        pole = klasy.Figury(a, 0, 0)
        obwod = klasy.Obwody(a, 0, 0)
        pole.kwadrat()
        obwod.obwod_kwadratu()
    elif wybor == 2:
        a = int(input("Wpisz długość pierwszego boku: "))
        b = int(input("Wpisz długość drugiego boku: "))
        pole = klasy.Figury(a, b, 0)
        obwod = klasy.Obwody(a, b, 0)
        pole.prostokat()
        obwod.obwod_prostokata()
    elif wybor == 3:
        a = int(input("Wpisz długość podstawy: "))
        h = int(input("Wpisz wysokość: "))
        pole = klasy.Figury(a, 0, h)
        obwod = klasy.Obwody(a, 0, 0)
        pole.romb()
        obwod.obwod_rombu()
    elif wybor == 4:
        a = int(input("Wpisz długość podstaw: "))
        b = int(input("Wpisz długość boków: "))
        h = int(input("Wpisz wysokość: "))
        pole = klasy.Figury(a, b, h)
        obwod = klasy.Obwody(a, b, h)
        pole.rownoleglobok()
        obwod.obwod_rownolegloboku()
    elif wybor == 5:
        a = int(input("Wpisz długość podstawy: "))
        h = int(input("Wpisz wysokość: "))
        pole = klasy.Figury(a, 0, h)
        obwod = klasy.Obwody(a, 0, h)
        pole.trojkat()
        obwod.obwod_trojkata()
    elif wybor == 6:
        a = int(input("Wpisz długość pierwszego boku a: "))
        b = int(input("Wpisz długość drugiego boku b: "))
        h = int(input("Wpisz wysokość: "))
        pole = klasy.Figury(a, b, h)
        obwod = klasy.Obwody(a, b, h)
        pole.trapez()
        obwod.obwod_trapezu()
    elif wybor == 7:
        print("Dziękuję za skorzystanie!")
        petla = False
        break






