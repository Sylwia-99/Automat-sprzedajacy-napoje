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
