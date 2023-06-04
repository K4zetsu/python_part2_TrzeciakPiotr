import mod1
        

while True:
    print("1. dodawanie")
    print("2. odejmowanie")
    print("3. mnożenie")
    print("4. dzielenie")
    print("0. koniec")
    try:
        wybor = int(input("Którą operację chcesz wykonać?: "))
    except ValueError:
        print("Zły format danych, spróbuj ponownie.")
        continue
    if wybor == 1:
        try:
            a = int(input("wpisz pierwszą liczbę: "))
            b = int(input("wpisz drugą liczbę: "))
        except ValueError:
            print("Zły format danych, spróbuj ponownie.")
            continue
        mod1.dodawanie(a, b)
    elif wybor == 2:
        try:
            a = int(input("wpisz pierwszą liczbę: "))
            b = int(input("wpisz drugą liczbę: "))
        except ValueError:
            print("Zły format danych, spróbuj ponownie.")
            continue
        mod1.odejmowanie(a, b)
    elif wybor == 3:
        try:
            a = int(input("wpisz pierwszą liczbę: "))
            b = int(input("wpisz drugą liczbę: "))
        except ValueError:
            print("Zły format danych, spróbuj ponownie.")
            continue
        mod1.mnozenie(a, b)
    elif wybor == 4:
        try:
            a = int(input("wpisz pierwszą liczbę: "))
            b = int(input("wpisz drugą liczbę: "))
        except ValueError:
            print("Zły format danych, spróbuj ponownie.")
            continue
        try:
            mod1.dzielenie(a, b)
        except ZeroDivisionError:
            print("Nie możesz cholero dzielić przez 0!!1")
    elif wybor == 0:
        print("Dziękuję za korzystanie z naszych usług!!")
        break
    elif wybor > 4 or wybor < 0:
        print("Wybrałeś nieistniejącą opcję, spróbuj ponownie.")
        continue