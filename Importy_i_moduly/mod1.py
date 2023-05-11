def dodawanie(a, b):
    wynik = a + b
    print(a, "+", b, "=", wynik)

def odejmowanie(a, b):
    wynik = a - b
    print(a, "-", b, "=", wynik)

def mnozenie(a, b):
    wynik = a * b
    print(a, "*", b, "=", wynik)

def dzielenie(a, b):
    if b == 0:
        print("NIE MOŻESZ DZIELIĆ PRZEZ 0 POTWORZE!!")
        exit
    wynik = a / b
    print(a, ":", b, "=", wynik)