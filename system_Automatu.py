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

