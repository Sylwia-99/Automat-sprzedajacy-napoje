from enum import Enum


class PojemnikMonet:
    """
    klasa PojemnikMonet reprezentuje pojemnik na pieniadze
    Zmienne:
        Monety:dict zmienna odpowiedzialna za przechowywanie monet
    Metody:
        dodaj_monety(Monety:monety) Dodaje monety do pojemnika na pieniadze.
        zwroc_wartosc(wartoscDoWydania) Zwraca monetyDoWydania czyli wartosc,
                którą wyciągam z pojemnika na pieniądze lub False,
                jeśli nie jest możliwe wydanie reszty(np, gdy nie ma w pojemniku odpowiednich monet)
    """
    Monety = {1: 70,
              2: 80,
              5: 90,
              10: 50,
              20: 40,
              50: 90,
              100: 50,
              200: 30,
              500: 20}

    def __init__(self):
        """
        konsturktor klasy
        """

    def dodaj_monety(self, monety):
        """
        Dodaje monety do pojemnika na pieniądze.
        :param monety: monety:Monety które zostały wrzucone do automatu
        """
        for wartosc, ilosc in monety.items():
            self.Monety[wartosc] += ilosc

    def zwroc_wartosc(self, wartosc_do_wydania):
        """
        Wyciaga monety z pojemnika na pieniądze.
        :param wartosc_do_wydania: wartość do wydania reszty
        :return: monetyDoWydania lub False, jeśli nie da się wydać reszty
        """
        wartosci_monet = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        monety_do_wydania = {w: 0 for w in wartosci_monet}  # zeruje monety w schowku
        while wartosc_do_wydania > 0:
            wart_monety = 0
            for i in wartosci_monet:
                if i <= wartosc_do_wydania and self.Monety[i] > 0:
                    wart_monety = i  # wybrane z kasetki monety
                    wartosc_do_wydania -= i  # obnizam wartosc do wydania o aktualną wartosc monety
                    self.Monety[i] -= 1  # zmniejszam ilosc wartosci monety w pojemniku na monety
                    break
            if wart_monety == 0:  # nie da sie wydac takiej reszty
                break
            monety_do_wydania[wart_monety] += 1
        if wartosc_do_wydania == 0:  # cala reszta moze byc wydana
            return monety_do_wydania
        # zwracam monety do kasetki bo nie da sie wydac reszty
        for wart, ilosc in monety_do_wydania.items():
            self.Monety[wart] += ilosc
            # informacja, ze nie da sie wydac reszty
            return False


class PojemnikProduktow:
    """
    Klasa PojemnikProduktow reprezentuje pojemnik na produkty.
    Zmienne:
        ListaProduktow:dict Przechowuje produkty dostepne w Automacie.
        Jest to zagnieżdzony slownik, ktory przechowuje informacje takie, jak:
        numer produktu,nazwe,cene i ilosc produktow w pojemniku na produkty
    Metody:
        czy_jest(numer) Sprawdza, czy jest produkt o danym numerze.
        cena(numer) Zwraca cene produktu o danym numerze.
        nazwa(numer) Zwraca nazwę produktu o danym numerze.
        zmniejsz_i_wypisz(numer) Zmniejsza ilosc produktow w pojemniku na produkty i zwraca informacje o nim.
    """
    ListaProduktow = {"30": {"nazwa": "woda gazowana", "cena": 351, "ilosc": 5},
                      "31": {"nazwa": "woda niegazowana", "cena": 351, "ilosc": 5},
                      "32": {"nazwa": "sok pomarańczowy", "cena": 406, "ilosc": 5},
                      "33": {"nazwa": "sok porzeczkowy", "cena": 406, "ilosc": 5},
                      "34": {"nazwa": "sok jabłkowy", "cena": 406, "ilosc": 5},
                      "35": {"nazwa": "mirinda", "cena": 450, "ilosc": 5},
                      "36": {"nazwa": "pepsi", "cena": 450, "ilosc": 5},
                      "37": {"nazwa": "pepsi light", "cena": 460, "ilosc": 5},
                      "38": {"nazwa": "cola", "cena": 380, "ilosc": 5},
                      "39": {"nazwa": "cola zero", "cena": 390, "ilosc": 5},
                      "40": {"nazwa": "nestea brzoskwiniowe", "cena": 469, "ilosc": 5},
                      "41": {"nazwa": "nestea cytrynowe", "cena": 469, "ilosc": 5},
                      "42": {"nazwa": "nestea zielona herbata", "cena": 469, "ilosc": 5},
                      "43": {"nazwa": "tymbark jakbło-mięta", "cena": 180, "ilosc": 5},
                      "44": {"nazwa": "tymbark pomarańcza-brzoskwinia", "cena": 180, "ilosc": 5},
                      "45": {"nazwa": "tymbark jabłko-wiśnia", "cena": 180, "ilosc": 5},
                      "46": {"nazwa": "tymbark jabłko-kiwi", "cena": 180, "ilosc": 5},
                      "47": {"nazwa": "sprite", "cena": 395, "ilosc": 5},
                      "48": {"nazwa": "7up", "cena": 400, "ilosc": 5},
                      "49": {"nazwa": "oranżada cytrynowa", "cena": 240, "ilosc": 5},
                      "50": {"nazwa": "oranżada wiśniowa", "cena": 240, "ilosc": 5}, }

    def __init__(self):
        """
        konstruktor klasy
        """

    def czy_jest(self, numer):
        """
        Sprawdza, czy w pojemniku na produkty jest produkt o danym numerze.
        :param numer: numer produktu
        :return: True jesli produkt jest w pojemniku na produkty. False, jeśli produktu w nim nie ma
        """
        if numer in self.ListaProduktow.keys() and self.ListaProduktow[numer]["ilosc"] > 0:
            return True
        return False

    def cena(self, numer):
        """
        Zwraca cene produktu o podanym numerze.
        :param numer: Numer produktu.
        :return:Cena podanego produktu lub False, jesli numeru nie ma w pojemniku na produkty.
        """
        if numer in self.ListaProduktow:
            return self.ListaProduktow[numer]["cena"]
        return False

    def nazwa(self, numer):
        """
        Zwraca nazwę produktu o danym numerze.
        :param numer: Numer produktu.
        :return:Nazwa produktu o podanym numerze.False, gdy numeru nie ma w pojemniku.
        """
        if numer in self.ListaProduktow:
            return self.ListaProduktow[numer]["nazwa"]
        return False

    def zmniejsz_i_wypisz(self, numer):
        """
        Zmniejsza ilosc produktow w pojemniku na produkty i zwraca informacje o nim.
        :param numer: Numer produktu.
        :return: Informacje o produkcie. False, jeśli numeru nie ma w pojemniku na produkty.
        """
        if numer in self.ListaProduktow and self.ListaProduktow[numer]["ilosc"] > 0:
            self.ListaProduktow[numer]["ilosc"] -= 1
            return self.ListaProduktow[numer]
        return False


class WyborKodu:
    """
    Klasa WyborKodu jest odpowiedzialna za wybor kodu(czyli numeru produktu).
    Zmienne:
        kod:String Przechowuje kod.
    Metody:
        wybierz(cyfra) Zwraca kod, jeśli jest 2-cyfrowy, inaczej False.
        stan() kod Zwraca kod lub False, jeśli w zmiennej kod nie jest nic zapisane.
        clear() Czyści kod(ustawia go na pusty string).
    """
    def __init__(self):
        """
        konstruktor klasy
        """

    kod = ""

    def wybierz(self, cyfra):
        """
        Sprawdza, czy jest coś już w kodzie zapisane i jeśli to była 2-cyfrowa liczba to zeruje kod,
        zapisuje wybraną cyfrę 1-cyfrową do kodu, jeśli jest mniejsza niż 2-cyfrowa to zwraca False.
        :param cyfra: cyfra oznacza cyrfę kodu, który reprezentuje numer napoju.
        :return: Zwraca kod, jeśli jest 2-cyfrowy, inaczej False.
        """
        if len(self.kod) == 2:
            self.clear()
        self.kod += cyfra
        if len(self.kod) == 2:
            return self.kod
        return False

    def stan(self):
        """
        Sprawdza, czy w kodzie jest cos zapisane.
        :return: kod lub False, jeśli w zmiennej kod nie jest nic zapisane.
        """
        if len(self.kod) != 0:
            return self.kod
        return False

    def clear(self):
        """
        Czyści kod(ustawia go na pusty string).
        """
        self.kod = ""


class Stan(Enum):
    """
    Ustawia stany.
    """
    wyborProduktu = 1
    wprowadzanieMonet = 2


class AutomatZnapojami:
    """
    Klasa Automat_z_napojami to główna klasa Automatu.
    Zmienne:
        monety_w_schowku:dict Przechowuje tymczasowo wrzucone pieniadze do kasetki.
        aktualna_kwota_w_schowku:int Przechowuje kwote w Schowku.
        wybrany_produkt:String Przechowuje kod(numer napoju).
    Metody:
        wybierz(cyfra) Przekazuje cyfre do wybor_kodu i jeśli wybrano kod i jest dostepny to wybiera numer napoju.
        wrzuc_monete(moneta) Dodaje monety to tymczasowego schowka.
        sprawdz_i_wydaj() Sprawdza czy pieniądze się zgadzają, jeśli tak wydaje reszte i produkt i True.
        przerwij() Zwraca natychmiast reszte(wrzucone do automatu pieniadze) i zeruje tymczasowy schowek monety_w_schowku oraz aktualna_kwota_w_schowku
        on_zwroc_reszte(fun_zwroc_reszte) Ustawia callback na fun_zwroc_reszte.
        on_zmiana_kodu(fun_zmiana_kodu) Ustawia callback na fun_zmiana_kodu.
        on_czekaj_na_pieniadze(fun_czekaj_na_pieniadze) Ustawia callback na fun_czekaj_na_pieniadze.
        on_ydaj_produkt(fun_wydaj_produkt) Ustawia callback na fun_wydaj_produkt.
        on_blad(fun_blad) Ustawia callback na fun_blad.
        on_niema_w_automacie(fun_nie_ma_w_automacie) Ustawia callback na fun_niema_w_automacie.
        on_tylko_odliczona_kwota(fun_tylko_odliczona_kwota) Ustawia callback na fun_tylko_odliczona_kwota.
    """
    def __init__(self):
        """
        konstruktor klasy, w którym wywołuje konstruktory powyższych klas
        tj. PojemnikMonet,PojemnikProduktow,WyborKodu
        """
        self.pojemnik_monet = PojemnikMonet()
        self.pojemnik_produktow = PojemnikProduktow()
        self.wybor_kodu = WyborKodu()

    # EVENTY
    fun_zwroc_reszte = None
    fun_zmiana_kodu = None
    fun_czekaj_na_pieniadze = None
    fun_wydaj_produkt = None
    fun_blad = None
    fun_nie_ma_w_automacie = None
    fun_tylko_odliczona_kwota = None

    # ZMIENNE
    PojemnikMonet = None
    PojemnikProduktow = None
    WyborKodu = None
    Stan = Stan.wyborProduktu  # ustawiam stan na wyborProduktu

    # schowek tymczasowo jest wyzerowany, bo przechowuje tymczasowo wrzucone pieniadze do kasetki
    nominaly = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    monety_w_schowku = {i: 0 for i in nominaly}  # tworze pusty schowek MonetyWSchowku
    aktualna_kwota_w_schowku = 0
    wybrany_produkt = ""  # kod produktu

    def wybierz(self, cyfra):
        """
        Przekazuje cyfre do wybor_kodu i jeśli wybrano kod, to gdy kod jest dostepny
        wybiera numer napoju.
        :param cyfra: cyfra Oznacza cyrfę kodu, który reprezentuje numer napoju.
        """
        kod = self.wybor_kodu.wybierz(cyfra)
        if kod is not False:  # jeśli wybrano kod
            if self.pojemnik_produktow.czy_jest(kod):  # i kod jest dostępny
                self.wybrany_produkt = kod  # zapisuje kod do wybranyProdukt
                self.Stan = Stan.wprowadzanieMonet  # ustawiam stan na wprowadzanieMonet
                self.fun_zmiana_kodu(kod)  # wykonuje EVENT funZmianaKodu
                self.fun_czekaj_na_pieniadze(self.pojemnik_produktow.cena(kod))  # wykonuje EVENT funCzekajNaPniedziadze
            else:
                self.fun_nie_ma_w_automacie(kod)  # wykonuje EVENT z informacją o braku produktu w Automacie
        else:
            self.fun_zmiana_kodu(self.wybor_kodu.stan())  # wykonuje EVENT zmiana kodu

    def wrzuc_monete(self, moneta):
        """
        Dodaje monety to tymczasowego schowka.
        :param moneta: moneta, która jest wrzucana do automatu.
        """
        self.monety_w_schowku[moneta] += 1  # dodaje pieniadze do Schowka tymczasowego(MonetyWSchowku)
        self.aktualna_kwota_w_schowku += moneta  # zwiekszam akualnaKwotaWSchowku
        print("Pieniądze w schowku:" + str(self.aktualna_kwota_w_schowku / 100))  # informacje o pieniądzach w schowku
        if self.Stan == Stan.wprowadzanieMonet:  # gdy Stan jest ustawiony na wprowadzanieMonet
            self.sprawdz_i_wydaj()  # to wywoluje funkcje sprawdz_i_wydaj

    def sprawdz_i_wydaj(self):
        """
        Sprawdza czy pieniądze się zgadzają, jeśli tak wydaje reszte i produkt i True.
        :return: zwraca True jeśli sprawdzanie przebiegło prawidlowo w przeciwnym razie False
        """
        if self.aktualna_kwota_w_schowku >= self.pojemnik_produktow.cena(self.wybrany_produkt):  # jesli wystarczy kasy
            roznica = self.aktualna_kwota_w_schowku - self.pojemnik_produktow.cena(self.wybrany_produkt)
            # liczę róznicę kwoty w schowku i ceny danego produktu
            reszta = self.pojemnik_monet.zwroc_wartosc(roznica)  # prosze o reszte z kasetki
            if reszta is False:  # gdy nie da się wydać reszty
                self.fun_zwroc_reszte(self.monety_w_schowku)  # prosze o wrzuconą przed chwilą wartość
                # wykonuje EVENT funTylkoOdliczonaKwota() z informacją o podanie wyliczonej Kwoty
                self.fun_tylko_odliczona_kwota()
            else:
                self.pojemnik_monet.dodaj_monety(self.monety_w_schowku)  # dodaje monety z schowka do Pojemnika
                self.fun_zwroc_reszte(reszta)  # wykonuje EVENT funZwrocReszte
                produkt = self.pojemnik_produktow.zmniejsz_i_wypisz(self.wybrany_produkt)  # wypisuje info o Produkcie i zmniejszam jego ilosc w Pojemniku
                self.fun_wydaj_produkt(produkt["nazwa"])
            self.monety_w_schowku = {monety: 0 for monety in self.monety_w_schowku}  # zeruje monety w schowku
            self.aktualna_kwota_w_schowku = 0  # zeruje aktualna kwote w schowku tymczasowym
            self.Stan = Stan.wyborProduktu  # ustawiam stan na wyborProduktu
            return True
        return False

    def przerwij(self):
        """
        Zwraca natychmiast reszte(wrzucone do automatu pieniadze) i zeruje tymczasowy schowek monety_schowku oraz aktualna_kwota_w_schowku.
        """
        if self.Stan == Stan.wprowadzanieMonet:  # ustawiam stan na wprowadzanieMonet
            # wykonuje EVENT  funZwrocReszte czyli wyrzucanie monet ze schowka tymczasowego od razu
            self.fun_zwroc_reszte(self.monety_w_schowku)
            self.monety_w_schowku = {monety: 0 for monety in self.monety_w_schowku}  # zeruje monety w schowku
            self.aktualna_kwota_w_schowku = 0  # zeruje aktualna kwote w schowku tymczasowym
            self.Stan = Stan.wyborProduktu  # ustawiam stan na wyborProduktu

    # subskrybcja EVENTOW
    def on_zwroc_reszte(self, fun_zwroc_reszte):
        """
        Ustawia callback na fun_zwroc_reszte.
        :param fun_zwroc_reszte: callback
        """
        self.fun_zwroc_reszte = fun_zwroc_reszte

    def on_zmiana_kodu(self, fun_zmiana_kodu):
        """
        Ustawia callback na fun_zmiana_kodu.
        :param fun_zmiana_kodu: callback
        """
        self.fun_zmiana_kodu = fun_zmiana_kodu

    def on_czekaj_na_pieniadze(self, fun_czekaj_na_pieniadze):
        """
        Ustawia callback na fun_czekaj_na_pieniadze.
        :param fun_czekaj_na_pieniadze: callback
        """
        self.fun_czekaj_na_pieniadze = fun_czekaj_na_pieniadze

    def on_wydaj_produkt(self, fun_wydaj_produkt):
        """
        Ustawia callback na fun_wydaj_produkt.
        :param fun_wydaj_produkt: callback
        """
        self.fun_wydaj_produkt = fun_wydaj_produkt

    def on_blad(self, fun_blad):
        """
        Ustawia callback na fun_blad.
        :param fun_blad: callback
        """
        self.fun_blad = fun_blad

    def on_nie_ma_w_automacie(self, fun_nie_ma_w_automacie):
        """
        Ustawia callback na fun_nie_ma_w_automacie.
        :param fun_nie_ma_w_automacie: callback
        """
        self.fun_nie_ma_w_automacie = fun_nie_ma_w_automacie

    def on_tylko_odliczona_kwota(self, fun_tylko_odliczona_kwota):
        """
        Ustawia callback na fun_tylko_odliczona_kwota.
        :param fun_tylko_odliczona_kwota:  callback
        """
        self.fun_tylko_odliczona_kwota = fun_tylko_odliczona_kwota


if __name__ == "__main__":

    automat = AutomatZnapojami()
    automat.on_zwroc_reszte(lambda monety: print("Wydano reszte:", monety))
    automat.on_zmiana_kodu(lambda kod: print("Aktualny kod:", kod))
    automat.on_czekaj_na_pieniadze(lambda cena: print("Wrzuc pieniadze, cena produktu=", cena/100))
    automat.on_wydaj_produkt(lambda produkt: print("Wydano produkt:", produkt))
    automat.on_nie_ma_w_automacie(lambda kod: print("W automacie nie ma produktu z numerem", kod))
    automat.on_blad(lambda info: print(info))

    if automat.pojemnik_produktow.czy_jest("36") is False:
        print("w Automacie nie ma produktu 36")
    else:
        print("w Automacie jest produkt 36")
# Test 1
    print("\n Test 1")
    print("Cena produktu nr 36 wynosi", automat.pojemnik_produktow.cena("36")/100, "zl")
# Test 2
    print("\n Test 2")
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze, cena produktu=1.8
    automat.wrzuc_monete(100)  # Pieniadze w schowku: 1.0
    automat.wrzuc_monete(50)  # Pieniadze w schowku: 1.5
    automat.wrzuc_monete(20)  # Pieniadze w schowku: 1.7
    automat.wrzuc_monete(10)  # Pieniadze w schowku: 1.8
    # Wydano reszte:{500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}#Wydano produkt: tymbark jabłko-kiwi
# Test 3
    print("\n Test 3")
    automat.wybierz("3")  # Aktualny kod: 3
    automat.wybierz("5")  # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
    automat.wrzuc_monete(200)  # Pieniadze w schowku: 2.0
    automat.wrzuc_monete(200)  # Pieniadze w schowku: 4.0
    automat.wrzuc_monete(200)  # Pieniadze w schowku: 6.0
    # Wydano reszte: {500: 0, 200: 0, 100: 1, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} # Wydano produkt: mirinda
# Test 4
    print("\n Test 4")
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze,cena produktu= 1.8
    automat.wrzuc_monete(100)  # Pieniadze w schowku: 1.0
    automat.wrzuc_monete(50)  # Pieniadze w schowku: 1.5
    automat.wrzuc_monete(20)  # Pieniadze w schowku: 1.7
    automat.wrzuc_monete(10)  # Pieniadze w schowku: 1.8
    # {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod:46 #Wrzuc pieniadze, cena produktu= 1.8
    automat.wrzuc_monete(100)  # Pieniadze w schowku: 1.0
    automat.wrzuc_monete(50)  # Pieniadze w schowku: 1.5
    automat.wrzuc_monete(20)  # Pieniadze w schowku: 1.7
    automat.wrzuc_monete(10)  # Pieniadze w schowku: 1.8
    # {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze,cena produktu= 1.8
    automat.wrzuc_monete(100)  # Pieniadze w schowku: 1.0
    automat.wrzuc_monete(50)  # Pieniadze w schowku: 1.5
    automat.wrzuc_monete(20)  # Pieniadze w schowku: 1.7
    automat.wrzuc_monete(10)  # Pieniadze w schowku: 1.8
    # {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze, cena produktu= 1.8
    automat.wrzuc_monete(100)  # Pieniadze w schowku: 1.0
    automat.wrzuc_monete(50)  # Pieniadze w schowku: 1.5
    automat.wrzuc_monete(20)  # Pieniadze w schowku: 1.7
    automat.wrzuc_monete(10)  # Pieniadze w schowku: 1.8
    # {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # W automacie nie ma produktu z numerem 46
# Test 5
    print("\n Test 5")
    automat.wybierz("9")  # Aktualny kod: 9
    automat.wybierz("9")  # W automacie nie ma produktu z numerem 99
    automat.wybierz("1")  # Aktualny kod: 1
    automat.wybierz("9")  # W automacie nie ma produktu z numerem 19
# Test 6
    print("\n Test 6")
    automat.wybierz("3")  # Aktualny kod: 3
    automat.wybierz("5")  # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
    automat.wrzuc_monete(200)  # Pieniadze w schowku: 2.0
    automat.wrzuc_monete(200)  # Pieniadze w schowku: 4.0
    automat.przerwij()  # Wydano reszte: {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 2, 500: 0}
# Test 7
    print("\n Test 7")
    automat.wrzuc_monete(50)  # Pieniądze w schowku:0.5
    automat.wybierz("3")  # Aktualny kod: 3
    automat.wybierz("5")  # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
    automat.wrzuc_monete(200)  # Pieniadze w schowku: 2.5
    automat.wrzuc_monete(200)  # Pieniadze w schowku: 4.5
    # Wydano reszte: {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} Wydano produkt: mirinda
    automat.wybierz("3")  # Aktualny kod: 3
    automat.wybierz("5")  # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
# Test 8
    print("\n Test 8")
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("5")  # Aktualny kod: 45 # Wrzuc pieniadz, cena produktu= 1.8
    for i in range(0, 180):
        automat.wrzuc_monete(1)
        # Pieniadze w schowku: ... #Wydano reszte: {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
        # Wydano produkt: tymbark jabłko-wiśnia
