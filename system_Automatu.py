from enum import Enum
class PojemnikMonet:
    """
    klasa PojemnikMonet reprezentuje pojemnik na pieniadze
    Zmienne:
        Monety:dict zmienna odpowiedzialna za przechowywanie monet
    Metody:
        dodajMonety(Monety:monety) dodaje monety do pojemnika na pieniadze
        zwrocWartosc(wartoscDoWydania) zwraca monetyDoWydania czyli wartosc, którą wyciągam z pojemnika na pieniądze
                                         lub False, jeśli nie jest możliwe wydanie reszty(np, gdy nie ma w pojemniku odpowiednich monet)
    """
    Monety={1:70,
            2:80,
            5:90,
            10:50,
            20:40,
            50:90,
            100:50,
            200:30,
            500:20}
    def __init__(self):
        """
        konsturktor klasy
        """
        pass

    def dodajMonety(self,monety):
        """
        dodaje monety do pojemnika na pieniądze
        :param monety: monety:Monety które zosatły wrzucone do automatu
        """
        for wartosc,ilosc in monety.items():
            self.Monety[wartosc]+=ilosc

    def zwrocWartosc(self,wartoscDoWydania):
        """
        wyciaga monety z pojemnika na pieniądze
        :param wartoscDoWydania: wartość do wydania reszty
        :return: monetyDoWydania lub False, jeśli nie da się wydać reszty
        """
        wartosciMonet=[500,200,100,50,20,10,5,2,1]
        monetyDoWydania={w:0 for w in wartosciMonet} #dictionary comprehension zeruje monety w schowku MonetyDoWydania
        while wartoscDoWydania>0:
            wartMonety=0
            for x in wartosciMonet:
                if x <= wartoscDoWydania and self.Monety[x] >0:
                    wartMonety=x #wybrane z kasetki monety
                    wartoscDoWydania-=x #obnizam wartosc do wydania o aktualną wartosc monety
                    self.Monety[x]-=1 #zmniejszam ilosc aktualnej wartosci moenty w pojemniku na monety
                    break
            if wartMonety==0: #nie da sie wydac takiej reszty
                break
            monetyDoWydania[wartMonety]+=1
        if wartoscDoWydania==0: #cala reszta moze byc wydana
            return monetyDoWydania
        else: #zwracam monety do kasetki bo nie da sie wydac reszty
            for wart,ilosc in monetyDoWydania.items():
                self.Monety[wart]+=ilosc
                # informacja, ze nie da sie wydac reszty
                return False

class PojemnikProduktow:
    """
    klasa PojemnikProduktow reprezentuje pojemnik na produkty
    Zmienne:
        ListaProduktow:dict zmienna odpowiedzialna za przechowywanie produktow dostepnych w Automacie
        Jest to zagnieżdzony slownik, ktory przechowuje informacje takie, jak: numer produktu,nazwe,cene i ilosc produktow w pojemniku na produkty
    Metody:
        czyjest(numer) sprawdza, czy jest produkt o danym numerze
        cena(numer) zwraca cene produktu o danym numerze
        nazwa(numer) nazwa zwraca nazwę produktu o danym numerze
        zmniejsziwypisz(numer) zmniejsza ilosc produktow w pojemniku na produkty i zwraca informacje o nim
    """
    ListaProduktow={"30":{"nazwa":"woda gazowana","cena":351,"ilosc":5},
                    "31":{"nazwa":"woda niegazowana","cena":351,"ilosc":5},
                    "32":{"nazwa":"sok pomarańczowy","cena":406,"ilosc":5},
                    "33":{"nazwa":"sok porzeczkowy","cena":406,"ilosc":5},
                    "34":{"nazwa":"sok jabłkowy","cena":406,"ilosc":5},
                    "35":{"nazwa":"mirinda","cena":450,"ilosc":5},
                    "36":{"nazwa":"pepsi","cena":450,"ilosc":5},
                    "37":{"nazwa":"pepsi light","cena":460,"ilosc":5},
                    "38":{"nazwa":"cola","cena":380,"ilosc":5},
                    "39":{"nazwa":"cola zero","cena":390,"ilosc":5},
                    "40":{"nazwa":"nestea brzoskwiniowe","cena":469,"ilosc":5},
                    "41":{"nazwa":"nestea cytrynowe","cena":469,"ilosc":5},
                    "42":{"nazwa":"nestea zielona herbata","cena":469,"ilosc":5},
                    "43":{"nazwa":"tymbark jakbło-mięta","cena":180,"ilosc":5},
                    "44":{"nazwa":"tymbark pomarańcza-brzoskwinia","cena":180,"ilosc":5},
                    "45":{"nazwa":"tymbark jabłko-wiśnia","cena":180,"ilosc":5},
                    "46":{"nazwa":"tymbark jabłko-kiwi","cena":180,"ilosc":5},
                    "47":{"nazwa":"sprite","cena":395,"ilosc":5},
                    "48":{"nazwa":"7up","cena":400,"ilosc":5},
                    "49":{"nazwa":"oranżada cytrynowa","cena":240,"ilosc":5},
                    "50":{"nazwa":"oranżada wiśniowa","cena":240,"ilosc":5},
    }
    def __init__(self):
        """
        konstruktor klasy
        """
        pass

    def czyjest(self,numer):
        """
        sprawdza, czy jest produkt o danym numerze w pojemniku na produkty
        :param numer: numer produktu
        :return: True jesli produkt jest w pojemniku na produkty lub False, jeśli produktu w nim nie ma
        """
        if numer in self.ListaProduktow.keys() and self.ListaProduktow[numer]["ilosc"]>0:
            return True
        else:
            return False

    def cena(self, numer):
        """
        zwraca cene produktu o podanym numerze
        :param numer: numer produktu
        :return:Cena podanego produktu lub False, jesli numeru nie ma w pojemniku na produkty
        """
        if numer in self.ListaProduktow:
            return self.ListaProduktow[numer]["cena"]
        else:
            return False

    def nazwa(self,numer):
        """
        nazwa zwraca nazwę produktu o danym numerze
        :param numer: numer produktu
        :return:Nazwa produktu o podanym numerze lub False, jesli numeru nie ma w pojemniku na produkty
        """
        if numer in self.ListaProduktow:
            return self.ListaProduktow[numer]["nazwa"]
        else:
            return False

    def zmniejsziwypisz(self,numer):
        """
        zmniejsza ilosc produktow w pojemniku na produkty i zwraca informacje o nim
        :param numer: numer produktu
        :return: Informacje o produkcie lub False, jesli numeru nie ma w pojemniku na produkty
        """
        if numer in self.ListaProduktow and self.ListaProduktow[numer]["ilosc"]>0:
            self.ListaProduktow[numer]["ilosc"]-=1
            return self.ListaProduktow[numer]
        return False

class WyborKodu:
    """
    klasa WyborKodu jest odpowiedzialna za wybor kodu(czyli numeru produktu)
    Zmienne:
        kod:String zmienna odpowiedzialna za przechowywanie kodu
    Metody:
        wybierz(cyfra) zwraca kod, jeśli jest 2-cyfrowy, inaczej False
        stan() kod zwraca kod lub False, jeśli w zmiennej kod nie jest nic zapisane
        clear() czyści kod(ustawia go na pusty string)
    """
    def __init__(self):
        """
        konstruktor klasy
        """
        pass

    kod=""
    def wybierz(self,cyfra):
        """
        sprawdza, czy jest coś już w kodzie zapisane i jeśli to była 2-cyfrowa liczba to zeruje kod
        zapisuje wybraną cyfrę 1-cyfrową do kodu, jesli jest mniejsza niż 2-cyfrowa to zwraca False
        :param cyfra: cyfra oznacza cyrfę kodu, który reprezentuje numer napoju
        :return: zwraca kod, jeśli jest 2-cyfrowy, inaczej False
        """
        if len(self.kod)==2:
            self.clear()
        self.kod+=cyfra
        if len(self.kod)==2:
            return self.kod
        else:
            return False

    def stan(self):
        """
        sprawdza, czy w kodzie jest cos zapisane
        :return: kod lub False, jeśli w zmiennej kod nie jest nic zapisane
        """
        if len(self.kod)!=0:
            return self.kod
        else:
            return False

    def clear(self):
        """
        czyści kod(ustawia go na pusty string)
        """
        self.kod = ""

class Stan(Enum):
    wyborProduktu=1
    wprowadzanieMonet=2


class Automat_z_napojami:
    """
    klasa Automat_z_napojami to główna klasa Automatu
    Zmienne:
        MonetyWSchowku:dict zmienna, która przechowuje tymczasowo wrzucone pieniadze do kasetki
        aktualnaKwotaWSchowku:int zmienna, która przechowuje kwote w Schowku
        wybranyProdukt:String zmienna, która przechowuje kod(numer napoju)
    Metody:
        wybierz(cyfra) przekazuje cyfre do wyborKodu i jeśli wybrano kod, to gdy kod jest dostepny
        wybiera numer napoju
        wrzucMonete(moneta) dodaje monety to tymczasowego schowka
        sprawdzIWydaj() Sprawdza czy pieniądze się zgadzają, jeśli tak wydaje reszte i produkt i True inaczej False
        przerwij() funkcja zwraca natychmiast reszte(a w zasadzie wrzucone do automatu pieniadze) i zeruje tymczasowy schowek MonetyWSchowku oraz aktualnaKwotaWSchowku
        onZwrocReszte(funZwrocReszte) ustawia callback na funZwrocReszte
        onZmianaKodu(funZmianaKodu) ustawia callback na funZmianaKodu
        onCzekajNaPieniadze(funCzekajNaPieniadze) ustawia callback na funCzekajNaPieniadze
        onWydajProdukt(funWydajProdukt) ustawia callback na funWydajProdukt
        onBlad(funBlad) ustawia callback na funBlad
        onNiemaWAautomacie(funNiemaWAautomacie) ustawia callback na funNiemaWAautomacie
        onTylkoOdliczonaKwota(funTylkoOdliczonaKwota) ustawia callback na funTylkoOdliczonaKwota
    """
    def __init__(self):
        """
        konstruktor klasy, w którym wywołuje konstruktory powyższych klas
        tj. PojemnikMonet,PojemnikProduktow,WyborKodu
        """
        self.pojemnikMonet = PojemnikMonet()
        self.pojemnikProduktow = PojemnikProduktow()
        self.wyborKodu = WyborKodu()

    #EVENTY
    funZwrocReszte=None
    funZmianaKodu=None
    funCzekajNaPieniadze=None
    funWydajProdukt=None
    funBlad=None
    funNiemaWAautomacie=None
    funTylkoOdliczonaKwota=None
    funInformacje=None

    #ZMIENNE
    PojemnikMonet=None
    PojemnikProduktow=None
    WyborKodu=None
    Stan=Stan.wyborProduktu #ustawiam stan na wyborProduktu

    # schowek tymczasowo jest wyzerowany, bo przechowuje tymczasowo wrzucone pieniadze do kasetki
    nominaly = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    MonetyWSchowku = {i: 0 for i in nominaly} #dictionary comprehension tworze pusty schowek MonetyWSchowku
    aktualnaKwotaWSchowku=0
    wybranyProdukt="" #kod produktu

    def wybierz(self,cyfra):
        """
        przekazuje cyfre do wyborKodu i jeśli wybrano kod, to gdy kod jest dostepny
        wybiera numer napoju
        :param cyfra: cyfra oznacza cyrfę kodu, który reprezentuje numer napoju
        """
        kod=self.wyborKodu.wybierz(cyfra)
        if kod !=False: #jeśli wybrano kod
            if self.pojemnikProduktow.czyjest(kod): # i kod jest dostępny
                self.wybranyProdukt=kod #zapisuje kod do wybranyProdukt
                self.Stan = Stan.wprowadzanieMonet #ustawiam stan na wprowadzanieMonet
                self.funZmianaKodu(kod) #wykonuje EVENT funZmianaKodu
                self.funCzekajNaPieniadze(self.pojemnikProduktow.cena(kod)) #wykonuje EVENT funCzekajNaPniedziadze
            else:
                self.funNiemaWAautomacie(kod) # wykonuje EVENT funNiemaWAutomacie z informacją o braku produktu w Automacie
        else:
            self.funZmianaKodu(self.wyborKodu.stan()) #wykonuje EVENT zmiana kodu

    def wrzucMonete(self,moneta):
        """
        dodaje monety to tymczasowego schowka
        :param moneta: moneta, która jest wrzucana do automatu
        """
        self.MonetyWSchowku[moneta]+=1 #dodaje pieniadze do Schowka tymczasowego(MonetyWSchowku)
        self.aktualnaKwotaWSchowku+=moneta #zwiekszam akualnaKwotaWSchowku
        print("Pieniądze w schowku:" + str(self.aktualnaKwotaWSchowku / 100)) #wypisuje informacje o pieniądzach w schowku
        #print("Produkt:" + str(self.wybranyProdukt)) #wypisuje informacje o kodzie wybranego produktu
        if self.Stan == Stan.wprowadzanieMonet:  # gdy Stan jest ustawiony na wprowadzanieMonet
            self.sprawdzIWydaj()  # to wywoluje funkcje sprawdzIWydaj

    def sprawdzIWydaj(self):
        """
        Sprawdza czy pieniądze się zgadzają, jeśli tak wydaje reszte i produkt i True
        :return: zwraca True jeśli sprawdzanie przebiegło prawidlowo w przeciwnym razie False
        """
        if self.aktualnaKwotaWSchowku >= self.pojemnikProduktow.cena(self.wybranyProdukt):  # jesli aktualnaKwotaWSchowku jest wystarczajaca
            roznica = self.aktualnaKwotaWSchowku - self.pojemnikProduktow.cena(self.wybranyProdukt)  # liczę róznicę kwoty w schowku i ceny danego produktu
            reszta = self.pojemnikMonet.zwrocWartosc(roznica)  # prosze o reszte z kasetki
            if reszta == False:  # gdy nie da się wydać reszty
                self.funZwrocReszte(self.MonetyWSchowku)  # prosze o wrzuconą przed chwilą wartość
                self.funTylkoOdliczonaKwota()  # wykonuje EVENT funTylkoOdliczonaKwota() z informacją o podanie wyliczonej Kwoty
            else:
                self.pojemnikMonet.dodajMonety(self.MonetyWSchowku)  # dodaje monety z tymczasowego schowka do Pojemnika na pieniądze
                self.funZwrocReszte(reszta)  # wykonuje EVENT funZwrocReszte
                produkt = self.pojemnikProduktow.zmniejsziwypisz(self.wybranyProdukt)  # wypisuje info o Produkcie i zmniejszam jego ilosc w Pojemniku na produkty
                self.funWydajProdukt(produkt["nazwa"])
            self.MonetyWSchowku = {monety: 0 for monety in self.MonetyWSchowku}  # dictionary comprehension zeruje monety w tymczasowym schowku
            self.aktualnaKwotaWSchowku = 0  # zeruje aktualna kwote w schowku tymczasowym
            self.Stan = Stan.wyborProduktu  # ustawiam stan na wyborProduktu
            return True
        else:
            return False

    def przerwij(self):
        """
        funkcja zwraca natychmiast reszte(a w zasadzie wrzucone do automatu pieniadze) i zeruje tymczasowy schowek MonetyWSchowku oraz aktualnaKwotaWSchowku
        """
        if self.Stan==Stan.wprowadzanieMonet: #ustawiam stan na wprowadzanieMonet
            self.funZwrocReszte(self.MonetyWSchowku) #wykonuje EVENT  funZwrocReszte czyli wyrzucanie monet ze schowka tymczasowego od razu
            self.MonetyWSchowku={monety:0 for monety in self.MonetyWSchowku} #dictionary comprehension zeruje monety w tymczasowym schowku
            self.aktualnaKwotaWSchowku=0 #zeruje aktualna kwote w schowku tymczasowym
            self.Stan=Stan.wyborProduktu #ustawiam stan na wyborProduktu

    #subskrybcja EVENTOW
    def onZwrocReszte(self,funZwrocReszte):
        """
        ustawia callback na funZwrocReszte
        :param funZwrocReszte: callback
        """
        self.funZwrocReszte=funZwrocReszte

    def onZmianaKodu(self,funZmianaKodu):
        """
        ustawia callback na funZmianaKodu
        :param funZmianaKodu: callback
        """
        self.funZmianaKodu=funZmianaKodu

    def onCzekajNaPieniadze(self,funCzekajNaPieniadze):
        """
        ustawia callback na funCzekajNaPieniadze
        :param funCzekajNaPieniadze: callback
        """
        self.funCzekajNaPieniadze=funCzekajNaPieniadze

    def onWydajProdukt(self,funWydajProdukt):
        """
        ustawia callback na funWydajProdukt
        :param funWydajProdukt: callback
        """
        self.funWydajProdukt=funWydajProdukt

    def onBlad(self,funBlad):
        """
        ustawia callback na funBlad
        :param funBlad: callback
        """
        self.funBlad=funBlad

    def onNiemaWAautomacie(self,funNiemaWAautomacie):
        """
        ustawia callback na funNiemaWAautomacie
        :param funNiemaWAautomacie: callback
        """
        self.funNiemaWAautomacie=funNiemaWAautomacie

    def onTylkoOdliczonaKwota(self,funTylkoOdliczonaKwota):
        """
        ustawia callback na funTylkoodliczonaKwota
        :param funTylkoOdliczonaKwota:  callback
        """
        self.funTylkoOdliczonaKwota=funTylkoOdliczonaKwota



if __name__=="__main__":

    automat=Automat_z_napojami()
    automat.onZwrocReszte(lambda monety: print("Wydano reszte:",monety))
    automat.onZmianaKodu( lambda kod: print("Aktualny kod:", kod) )
    automat.onCzekajNaPieniadze( lambda cena: print("Wrzuc pieniadze, cena produktu=", cena/100))
    automat.onWydajProdukt( lambda produkt: print("Wydano produkt:", produkt) )
    automat.onNiemaWAautomacie(lambda kod: print("W automacie nie ma produktu z numerem",kod))
    automat.onBlad( lambda info: print(info) )

    if automat.pojemnikProduktow.czyjest("36") ==False:
        print("w Automacie nie ma produktu 36")
    else:
        print("w Automacie jest produkt 36")
###Test 1
    print("\n Test 1")
    print("Cena produktu nr 36 wynosi",automat.pojemnikProduktow.cena("36")/100,"zl")
###Test 2
    print("\n Test 2")
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze, cena produktu=1.8
    automat.wrzucMonete(100) #Pieniadze w schowku: 1.0
    automat.wrzucMonete(50) #Pieniadze w schowku: 1.5
    automat.wrzucMonete(20) #Pieniadze w schowku: 1.7
    automat.wrzucMonete(10) #Pieniadze w schowku: 1.8 #Wydano reszte:{500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}#Wydano produkt: tymbark jabłko-kiwi
###Test 3
    print("\n Test 3")
    automat.wybierz("3") # Aktualny kod: 3
    automat.wybierz("5") # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
    automat.wrzucMonete(200)#Pieniadze w schowku: 2.0
    automat.wrzucMonete(200)#Pieniadze w schowku: 4.0
    automat.wrzucMonete(200) #Pieniadze w schowku: 6.0 # Wydano reszte: {500: 0, 200: 0, 100: 1, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} # Wydano produkt: mirinda
###Test 4
    print("\n Test 4")
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze,cena produktu= 1.8
    automat.wrzucMonete(100) #Pieniadze w schowku: 1.0
    automat.wrzucMonete(50) #Pieniadze w schowku: 1.5
    automat.wrzucMonete(20) #Pieniadze w schowku: 1.7
    automat.wrzucMonete(10) #Pieniadze w schowku: 1.8 #{500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod:46 #Wrzuc pieniadze, cena produktu= 1.8
    automat.wrzucMonete(100) #Pieniadze w schowku: 1.0
    automat.wrzucMonete(50)#Pieniadze w schowku: 1.5
    automat.wrzucMonete(20)#Pieniadze w schowku: 1.7
    automat.wrzucMonete(10)#Pieniadze w schowku: 1.8 # {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze,cena produktu= 1.8
    automat.wrzucMonete(100) #Pieniadze w schowku: 1.0
    automat.wrzucMonete(50)#Pieniadze w schowku: 1.5
    automat.wrzucMonete(20)#Pieniadze w schowku: 1.7
    automat.wrzucMonete(10)#Pieniadze w schowku: 1.8 # {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze, cena produktu= 1.8
    automat.wrzucMonete(100) #Pieniadze w schowku: 1.0
    automat.wrzucMonete(50) #Pieniadze w schowku: 1.5
    automat.wrzucMonete(20) #Pieniadze w schowku: 1.7
    automat.wrzucMonete(10) #Pieniadze w schowku: 1.8 # {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  #W automacie nie ma produktu z numerem 46
###Test 5
    print("\n Test 5")
    automat.wybierz("9") # Aktualny kod: 9
    automat.wybierz("9") #W automacie nie ma produktu z numerem 99
    automat.wybierz("1") # Aktualny kod: 1
    automat.wybierz("9") # W automacie nie ma produktu z numerem 19
###Test 6
    print("\n Test 6")
    automat.wybierz("3")  # Aktualny kod: 3
    automat.wybierz("5")  # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
    automat.wrzucMonete(200) #Pieniadze w schowku: 2.0
    automat.wrzucMonete(200) #Pieniadze w schowku: 4.0
    automat.przerwij()#Wydano reszte: {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 2, 500: 0}
###Test 7
    print("\n Test 7")
    automat.wrzucMonete(50) #Pieniądze w schowku:0.5
    automat.wybierz("3")  # Aktualny kod: 3
    automat.wybierz("5")  # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
    automat.wrzucMonete(200) #Pieniadze w schowku: 2.5
    automat.wrzucMonete(200) #Pieniadze w schowku: 4.5 Wydano reszte: {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} Wydano produkt: mirinda
    automat.wybierz("3")  # Aktualny kod: 3
    automat.wybierz("5")  # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
###Test 8
    print("\n Test 8")
    automat.wybierz("4") # Aktualny kod: 4
    automat.wybierz("5") # Aktualny kod: 45 # Wrzuc pieniadz, cena produktu= 1.8
    for i in range(0,180):
        automat.wrzucMonete(1) #Pieniadze w schowku: ... #Wydano reszte: {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
                                #Wydano produkt: tymbark jabłko-wiśnia
