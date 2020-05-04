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
