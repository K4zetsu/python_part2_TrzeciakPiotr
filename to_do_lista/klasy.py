
import json
from datetime import date, datetime
class Lista:
    def __init__(self, Numer, Tytul, Termin, Opis, DzienTygodnia):
        self.numerID = Numer
        self.tytul = Tytul
        self.termin = Termin
        self.opis = Opis
        self.dzien = DzienTygodnia
    def dodajZadanie(self):
        idZadania = self.numerID
        tytulZadania = self.tytul
        terminZadania = self.termin
        opisZadania = self.opis
        Dzien_Tygodnia = self.dzien
        zadanie = [idZadania, tytulZadania, terminZadania, opisZadania, Dzien_Tygodnia]
        return zadanie
    def usunZadanie(self, do_usuniecia):
        with open("to_do_lista/lista_zadan.json", "r", encoding="utf-8") as plik:
            lista_zadan = json.load(plik)
        if do_usuniecia < 1 or do_usuniecia > len(lista_zadan):
            print("Nieprawidłowy numer zadania do usunięcia!")
        else:
            lista_zadan.pop(do_usuniecia - 1)
            with open("to_do_lista/lista_zadan.json", "w", encoding="utf-8") as plik:
                json.dump(lista_zadan, plik, ensure_ascii=False, indent=4)
                print("Zadanie numer {} zostało usunięte!".format(do_usuniecia))