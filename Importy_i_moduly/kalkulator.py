import mod1

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
        mod1.dzielenie(a, b)
    elif wybor == 0:
        print("Dziękuję za korzystanie z naszych usług!!")
        break