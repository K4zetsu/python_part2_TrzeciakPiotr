import mod1

class WrongNumberException(Exception):
    def __init__(self):
        super().__init__("Wybrałeś zły numer, nie jest on przypisany do żadnego działania")
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
        mod1.dodawanie(a, b)
    elif wybor == 2:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        mod1.odejmowanie(a, b)
    elif wybor == 3:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        mod1.mnozenie(a, b)
    elif wybor == 4:
        a = int(input("wpisz pierwszą liczbę: "))
        b = int(input("wpisz drugą liczbę: "))
        try:
            mod1.dzielenie(a, b)
        except ZeroDivisionError:
            print("Nie możesz cholero dzielić przez 0!!1")
    elif wybor == 0:
        print("Dziękuję za korzystanie z naszych usług!!")
        break
    elif wybor > 4 or wybor < 0:
        raise WrongNumberException