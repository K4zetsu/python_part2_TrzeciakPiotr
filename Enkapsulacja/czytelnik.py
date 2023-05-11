class Czytelnik:
    """Self to taki odnośnik pozwalający odnosić się do oiektów wewnątrz klasy, nie no nie wiem co to jest ale ponoć ważne więc dodawaj zawsze do siebie do projektu"""
    def __init__(self, czytelnik_imie: str,czytelnik_nazwisko: str, czytelnik_wiek: int, numer_karty: int, adres_zamieszkania: str):
        self.__czytelnik = self.stworz_czytelnika(czytelnik_imie, czytelnik_nazwisko)
        self.__wiek = czytelnik_wiek
        self.__karta = numer_karty
        self.__zamieszkanie = adres_zamieszkania
    def stworz_czytelnika(self, imie:str, nazwisko:str) -> dict[str, str]:
        return{"imie":imie, "nazwisko":nazwisko}
    def pobierz_czytelnika(self) -> dict[str, str]:
        return self.__czytelnik