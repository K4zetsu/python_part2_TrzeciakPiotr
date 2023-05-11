from os import path

dir_path = path.dirname(__file__)
nazwa_pliku = 'tekst.txt'
data_path = path.join(dir_path, nazwa_pliku)
with open(data_path, 'r', encoding='utf-8') as plik:
    linie = plik.readlines()
    
    x = linie[0].split(", ")
    print(x)