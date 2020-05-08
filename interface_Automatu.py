from system_Automatu import Automat_z_napojami #importuje moduł system_Automatu
from tkinter import*
automat = Automat_z_napojami() #wywoluje konsturktor głownej klasy systemu_Automatu
class Interfejs_automatu:
    def __init__(self):
        pass
    okno = Tk() #towrze główne okno
    okno.resizable(width=True, height=True)  # pozwalam na rozciaganie okna
    okno.configure(background='black') #ustalam tlo okna

    wpis0 = Entry(okno, width=30,background='silver',foreground='black') #tworze puste pole, ustawiam jego szerokosc, kolor tła i czcionki
    wpis0.grid(row=1, column=1, padx=1, pady=1)#ustalam ułożenie i wielkosc pola

    wpis = Entry(okno, width=30,background='silver',foreground='black') #tworze puste pole, ustawiam jego szerokosc, kolor tła i czcionki
    wpis.grid(row=7, column=1, padx=1, pady=1) #ustalam ułożenie i wielkosc pola

    def interfejs(self):
        etykieta1 = Label(self.okno, text='Automat z napojami',foreground="white",background='black') #tworze główną etykiete z tytułem Aplikacji, ustalam kolor tla i czcionki
        etykieta1.grid(row=0, column=1,padx=5, pady=5,sticky=W+S+E+N)#ustalam ułożenie etykiety
        etykieta1.config(font=("Arial", 16, "italic")) #ustalam rodzaj czcionki i jej wielkość

        etykieta2 = Label(self.okno, text='Wrzucona kwota',foreground="white",background='black') #tworze etykiete z tytułem Wrzucona kwota, ustalam kolor tla i czcionki
        etykieta2.grid(row=1, column=0,padx=1, pady=1,)#ustalam ułożenie etykiety
        etykieta2.config(font=("Arial", 13, "italic"))#ustalam rodzaj czcionki i jej wielkość

        etykieta3 = Label(self.okno, text='Wybrany numer',foreground="white",background='black') #tworze etykiete z tytułem Wybrany numer, ustalam kolor tla i czcionki
        etykieta3.grid(row=7, column=0,padx=4, pady=4)#ustalam ułożenie etykiety
        etykieta3.config(font=("Arial", 13, "italic"))#ustalam rodzaj czcionki i jej wielkość

        przycisk = Button(self.okno, text="Zamknij",command=self.zamknij)  # tworze przycisk Zamknij i ustalam obsługe jego kliknięcia
        przycisk.grid(row=22, column=2, padx=4, pady=4, sticky=E)  # ustalam ułożenie przycisku i jego wyrownanie
        przycisk.bind("<Button-1>", self.zamknij)  # ustalam,że przycisk reaguje na pliknięcie na niego myszką
        przycisk.config(font=("Arial", 10, "italic"), background="silver",foreground='red')  # ustalam rodzaj czcionki i jej wielkość oraz kolor przycisku i czcionki

        przycisk0 = Button(self.okno, text="Przerwij",command=self.zamknij)  # tworze przycisk Przerwij i ustalam obsługe jego kliknięcia
        przycisk0.grid(row=6, column=1, padx=4, pady=4)  # ustalam ułożenie przycisku
        przycisk0.bind("<Button-1>", self.zamknij)  # ustalam,że przycisk reaguje na pliknięcie na niego myszką
        przycisk0.config(font=("Arial", 12, "italic"), foreground="black",
                         background='silver')  # ustalam rodzaj czcionki i jej wielkość oraz kolor przycisku i czcionki

        # tworze przyciski do wrzucania monet i ustalam obsługe ich kliknięcia, oraz tytuł, rodzaj i wielkosc czcionki w tytule
        przycisk1 = Button(self.okno, text="1 gr", command=lambda: self.wrzucono_monete(1),
                           font=("Arial", 14, "italic"), foreground="white", background='black')
        przycisk2 = Button(self.okno, text="2 gr", command=lambda: self.wrzucono_monete(2),
                           font=("Arial", 14, "italic"), foreground="white", background='black')
        przycisk5 = Button(self.okno, text="5 gr", command=lambda: self.wrzucono_monete(5),
                           font=("Arial", 14, "italic"), foreground="white", background='black')
        przycisk10 = Button(self.okno, text="10 gr", command=lambda: self.wrzucono_monete(10),
                            font=("Arial", 14, "italic"), foreground="white", background='black')
        przycisk20 = Button(self.okno, text="20 gr", command=lambda: self.wrzucono_monete(20),
                            font=("Arial", 14, "italic"), foreground="white", background='black')
        przycisk50 = Button(self.okno, text="50 gr", command=lambda: self.wrzucono_monete(50),
                            font=("Arial", 14, "italic"), foreground="white", background='black')
        przycisk_1 = Button(self.okno, text="1 zł", command=lambda: self.wrzucono_monete(100),
                            font=("Arial", 14, "italic"), foreground="white", background='black')
        przycisk_2 = Button(self.okno, text="2 zł", command=lambda: self.wrzucono_monete(200),
                            font=("Arial", 14, "italic"), foreground="white", background='black')
        przycisk_5 = Button(self.okno, text="5 zł", command=lambda: self.wrzucono_monete(500),
                            font=("Arial", 14, "italic"), foreground="white", background='black')

        # ustalam położenie przycisków
        przycisk1.grid(row=2, column=0, padx=1, pady=1)
        przycisk2.grid(row=2, column=1, padx=1, pady=1)
        przycisk5.grid(row=2, column=2, padx=1, pady=1)

        przycisk10.grid(row=3, column=0, padx=1, pady=1)
        przycisk20.grid(row=3, column=1, padx=1, pady=1)
        przycisk50.grid(row=3, column=2, padx=1, pady=1)

        przycisk_1.grid(row=4, column=0, padx=1, pady=1)
        przycisk_2.grid(row=4, column=1, padx=1, pady=1)
        przycisk_5.grid(row=4, column=2, padx=1, pady=1)

        # tworze przyciski do wyboru numeru produktu i ustalam obsługe ich kliknięcia, oraz tytuł, rodzaj i wielkosc czcionki w tytule
        przyc1 = Button(self.okno, text="1", command=lambda: self.kliknieto_przycisk(1), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc2 = Button(self.okno, text="2", command=lambda: self.kliknieto_przycisk(2), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc3 = Button(self.okno, text="3", command=lambda: self.kliknieto_przycisk(3), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc4 = Button(self.okno, text="4", command=lambda: self.kliknieto_przycisk(4), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc5 = Button(self.okno, text="5", command=lambda: self.kliknieto_przycisk(5), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc6 = Button(self.okno, text="6", command=lambda: self.kliknieto_przycisk(6), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc7 = Button(self.okno, text="7", command=lambda: self.kliknieto_przycisk(7), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc8 = Button(self.okno, text="8", command=lambda: self.kliknieto_przycisk(8), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc9 = Button(self.okno, text="9", command=lambda: self.kliknieto_przycisk(9), font=("Arial", 14, "italic"),
                        foreground="white", background='black')
        przyc0 = Button(self.okno, text="0", command=lambda: self.kliknieto_przycisk(0), font=("Arial", 14, "italic"),
                        foreground="white", background='black')

        # ustalam położenie przycisków
        przyc1.grid(row=8, column=0, padx=1, pady=1)
        przyc2.grid(row=8, column=1, padx=1, pady=1)
        przyc3.grid(row=8, column=2, padx=1, pady=1)

        przyc4.grid(row=9, column=0, padx=1, pady=1)
        przyc5.grid(row=9, column=1, padx=1, pady=1)
        przyc6.grid(row=9, column=2, padx=1, pady=1)

        przyc7.grid(row=10, column=0, padx=1, pady=1)
        przyc8.grid(row=10, column=1, padx=1, pady=1)
        przyc9.grid(row=10, column=2, padx=1, pady=1)

        przyc0.grid(row=11, column=1, padx=1, pady=1)
    def run(self):
        self.okno.mainloop()#uruchamiam okno

    def zamknij(self,numer):
        self.okno.quit() #zamykam okno
        self.okno.destroy() #zwalniam zasoby zajete przez okno

    def wrzucono_monete(self,moneta):
        automat.wrzucMonete(moneta) #wywoluje funkcje wrzucMonete z klasy Automat_z_napojami

    def kliknieto_przycisk(self,numer):
        automat.wybierz(str(numer)) #wywoluje funkcje wybierz z klasy Automat_z_napojami


if __name__=="__main__":
    interfejs=Interfejs_automatu()
    interfejs.interfejs()
    interfejs.run()