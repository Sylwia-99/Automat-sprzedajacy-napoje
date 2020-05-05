from enum import Enum
class PojemnikMonet:
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
        pass

    def dodajMonety(self,monety):
        for wartosc,ilosc in monety.items():
            self.Monety[wartosc]+=ilosc

    def zwrocWartosc(self,wartoscDoWydania):
        wartosciMonet=[500,200,100,50,20,10,5,2,1]
        monetyDoWydania={}
        for w in wartosciMonet:
            monetyDoWydania[w]=0
        while wartoscDoWydania>0:
            wartMonety=0
            for x in wartosciMonet:
                if x <= wartoscDoWydania and self.Monety[x] >0:
                    wartMonety=x
                    wartoscDoWydania-=x
                    self.Monety[x]-=1
                    break
            if wartMonety==0:
                break
            monetyDoWydania[wartMonety]+=1
        if wartoscDoWydania==0:
            return monetyDoWydania
        else:
            for wart,ilosc in monetyDoWydania.items():
                self.Monety[wart]+=ilosc
                return False

class PojemnikProduktow:
    ListaProduktow={"30":{"nazwa":"woda gazowana","cena":351,"ilosc":5},
                    "31":{"nazwa":"woda niegazowana","cena":351,"ilosc":5},
                    "32":{"nazwa":"sok pomarańczowy","cena":406,"ilosc":5},
                    "33":{"nazwa":"sok porzeczkowy","cena":406,"ilosc":5},
                    "34":{"nazwa":"sok jabłkowy","cena":406,"ilosc":5},
                    "35":{"nazwa":"mirinda","cena":450,"ilosc":5},
                    "36":{"nazwa":"pepsi","cena":450,"ilosc":0},
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
        pass

    def czyjest(self,numer):
        if numer in self.ListaProduktow.keys() and self.ListaProduktow[numer]["ilosc"]>0:
            return True
        else:
            return False

    def cena(self, numer):
        if numer in self.ListaProduktow:
            return self.ListaProduktow[numer]["cena"]
        else:
            return False

    def nazwa(self,numer):
        if numer in self.ListaProduktow:
            return self.ListaProduktow[numer]["nazwa"]
        else:
            return False

    def zmniejsziwypisz(self,numer):
        if numer in self.ListaProduktow and self.ListaProduktow[numer]["ilosc"]>0:
            self.ListaProduktow[numer]["ilosc"]-=1
            return self.ListaProduktow[numer]
        return False

class WyborKodu:
    def __init__(self):
        pass

    kod=""
    def wybierz(self,cyfra):
        if len(self.kod)==2:
            self.clear()
        self.kod+=cyfra
        if len(self.kod)==2:
            return self.kod
        else:
            return False

    def stan(self):
        if len(self.kod)!=0:
            return self.kod
        else:
            return False

    def clear(self):
        self.kod = ""

class Stan(Enum):
    wyborProduktu=1
    wprowadzanieMonet=2


class Automat_z_napojami:
    def __init__(self):
        self.pojemnikMonet = PojemnikMonet()
        self.pojemnikProduktow = PojemnikProduktow()
        self.wyborKodu = WyborKodu()

    funZwrocReszte=None
    funZmianaKodu=None
    funCzekajNaPieniadze=None
    funWydajProdukt=None
    funBlad=None
    funNiemaWAautomacie=None
    funTylkoOdliczonaKwota=None
    funInformacje=None

    PojemnikMonet=None
    PojemnikProduktow=None
    WyborKodu=None
    Stan=Stan.wyborProduktu

    MonetyWSchowku={
        1:0,
        2:0,
        5:0,
        10:0,
        20:0,
        50:0,
        100:0,
        200:0,
        500:0
    }
    aktualnaKwotaWSchowku=0
    wybranyProdukt=""

    def wybierz(self,cyfra):
        kod=self.wyborKodu.wybierz(cyfra)
        if kod !=False:
            if self.pojemnikProduktow.czyjest(kod):
                self.wybranyProdukt=kod
                self.Stan = Stan.wprowadzanieMonet
                self.funZmianaKodu(kod)
                self.funCzekajNaPieniadze(self.pojemnikProduktow.cena(kod))
            else:
                self.funNiemaWAautomacie(kod)
        else:
            self.funZmianaKodu(self.wyborKodu.stan())

    def wrzucMonete(self,moneta):
        if self.Stan == Stan.wprowadzanieMonet:
            self.MonetyWSchowku[moneta]+=1
            self.aktualnaKwotaWSchowku+=moneta
            if self.aktualnaKwotaWSchowku>=self.pojemnikProduktow.cena(self.wybranyProdukt):
                roznica=self.aktualnaKwotaWSchowku-self.pojemnikProduktow.cena(self.wybranyProdukt)
                reszta=self.pojemnikMonet.zwrocWartosc(roznica)
                if reszta==False:
                    self.funZwrocReszte(self.MonetyWSchowku)
                    self.funTylkoOdliczonaKwota()
                else:
                    self.pojemnikMonet.dodajMonety(self.MonetyWSchowku)
                    self.funZwrocReszte(reszta)
                    produkt=self.pojemnikProduktow.zmniejsziwypisz(self.wybranyProdukt)
                    self.funWydajProdukt(produkt["nazwa"])
                for monety in self.MonetyWSchowku:
                    self.MonetyWSchowku[monety]=0
                self.aktualnaKwotaWSchowku = 0
                self.Stan =Stan.wyborProduktu
        else:
            self.funZwrocReszte({moneta: 1})

    def przerwij(self):
        if self.Stan==Stan.wprowadzanieMonet:
            self.funZwrocReszte(self.MonetyWSchowku)
            for monety in self.MonetyWSchowku:
                self.MonetyWSchowku[monety]=0
            self.aktualnaKwotaWSchowku=0
            self.Stan=Stan.wyborProduktu

    def onZwrocReszte(self,funZwrocReszte):
        self.funZwrocReszte=funZwrocReszte

    def onZmianaKodu(self,funZmianaKodu):
        self.funZmianaKodu=funZmianaKodu

    def onCzekajNaPieniadze(self,funCzekajNaPieniadze):
        self.funCzekajNaPieniadze=funCzekajNaPieniadze

    def onWydajProdukt(self,funWydajProdukt):
        self.funWydajProdukt=funWydajProdukt

    def onBlad(self,funBlad):
        self.funBlad=funBlad

    def onNiemaWAautomacie(self,funNiemaWAautomacie):
        self.funNiemaWAautomacie=funNiemaWAautomacie

    def onTylkoOdliczonaKwota(self,funTylkoOdliczonaKwota):
        self.funTylkoOdliczonaKwota=funTylkoOdliczonaKwota

    def onInformacje(self,funInformacje):
        self.onInformacje=funInformacje


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

    automat.wrzucMonete(50)  # Wydano reszte: {50: 1}
###Test 1
    print("Cena produktu nr 36 wynosi",automat.pojemnikProduktow.cena("36")/100,"zl")

###Test 2
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  #Wrzuc pieniadze, cena produktu=1.8
    automat.wrzucMonete(100)
    automat.wrzucMonete(50)
    automat.wrzucMonete(20)
    automat.wrzucMonete(10) #{500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}#Wydano produkt: tymbark jabłko-kiwi
###Test 3
    automat.wybierz("3") # Aktualny kod: 3
    automat.wybierz("5") # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
    automat.wrzucMonete(200)
    automat.wrzucMonete(200)
    automat.wrzucMonete(200) # Wydano reszte: {500: 0, 200: 0, 100: 1, 50: 1, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} # Wydano produkt: pepsi
###Test 4
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze,cena produktu= 1.8
    automat.wrzucMonete(100)
    automat.wrzucMonete(50)
    automat.wrzucMonete(20)
    automat.wrzucMonete(10)# {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod:46 #Wrzuc pieniadze, cena produktu= 1.8
    automat.wrzucMonete(100)
    automat.wrzucMonete(50)
    automat.wrzucMonete(20)
    automat.wrzucMonete(10)# {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze,cena produktu= 1.8
    automat.wrzucMonete(100)
    automat.wrzucMonete(50)
    automat.wrzucMonete(20)
    automat.wrzucMonete(10)# {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  # Aktualny kod: 46 #Wrzuc pieniadze, cena produktu= 1.8
    automat.wrzucMonete(100)
    automat.wrzucMonete(50)
    automat.wrzucMonete(20)
    automat.wrzucMonete(10) # {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0} #Wydano produkt: tymbark jabłko-kiwi
    automat.wybierz("4")  # Aktualny kod: 4
    automat.wybierz("6")  #W automacie nie ma produktu z numerem 46
###Test 5
    automat.wybierz("9") # Aktualny kod: 9
    automat.wybierz("9") #W automacie nie ma produktu z numerem 99
    automat.wybierz("1") # Aktualny kod: 1
    automat.wybierz("9") # W automacie nie ma produktu z numerem 19
###Test 6
    automat.wybierz("3")  # Aktualny kod: 3
    automat.wybierz("5")  # Aktualny kod: 35 # Wrzuc pieniadze, cena produktu= 4.5
    automat.wrzucMonete(200)
    automat.wrzucMonete(200)
    automat.przerwij()#Wydano reszte: {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 2, 500: 0}
###Test 7


###Test 8
    automat.wybierz("4") # Aktualny kod: 4
    automat.wybierz("5") # Aktualny kod: 45 # Wrzuc pieniadz, cena produktu= 1.8
    for i in range(0,180):
        automat.wrzucMonete(1) #Wydano reszte: {500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
                                #Wydano produkt: tymbark jabłko-wiśnia
