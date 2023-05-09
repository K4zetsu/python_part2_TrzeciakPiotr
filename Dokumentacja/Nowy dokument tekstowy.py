"""poniższe funkcje słuzą do zbudowania menu wyboru, każda funkcja zawiera osobne działanie które jest wybierane """
def dodawanie(a: float, b: float) -> None:
    """Wykonuje dodawanie"""
    wynik = a + b
    print(a, "+", b, "=", wynik)

def odejmowanie(a: float, b: float) -> None:
    """Wykonuje odejmowanie"""
    wynik = a - b
    print(a, "-", b, "=", wynik)

def mnozenie(a: float, b: float) -> None:
    """Wykonuje mnożenie"""
    wynik = a * b
    print(a, "*", b, "=", wynik)

def dzielenie(a: float, b: float) -> None:
    """Wykonuje dzielenie ze sprawdzeniem warunku zakazu dzielenia przez 0"""
    if b == 0:
        print("NIE MOŻESZ DZIELIĆ PRZEZ 0 POTWORZE!!")
        exit
    wynik = a / b
    print(a, ":", b, "=", wynik)

"""poniższa pętla spina wszystkie te funkcje w całość, tworzy menu i ma działać do momentu wybrania przez użytkownika opcji 0. koniec
która zawiera funkcję break"""

while True:
    print("1. dodawanie")
    print("2. odejmowanie")
    print("3. mnożenie")
    print("4. dzielenie")
    print("0. koniec")

    wybor = int(input("Którą operację chcesz wykonać?: "))

    if wybor == 1:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        dodawanie(a, b)
    elif wybor == 2:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        odejmowanie(a, b)
    elif wybor == 3:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        mnozenie(a, b)
    elif wybor == 4:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        dzielenie(a, b)
    elif wybor == 0:
        print("Dziękuję za korzystanie z naszych usług!!")
        break