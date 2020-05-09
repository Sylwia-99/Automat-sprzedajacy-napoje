from system_Automatu import Automat_z_napojami #importuje moduł system_Automatu
from tkinter import*
import time
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

        # dodaje przyciski do wrzucania monet do zmiennej klasy Interfejs_automatu przyciski_monety(listy)
        self.przyciski_monety.append(przycisk1)
        self.przyciski_monety.append(przycisk2)
        self.przyciski_monety.append(przycisk5)
        self.przyciski_monety.append(przycisk10)
        self.przyciski_monety.append(przycisk20)
        self.przyciski_monety.append(przycisk50)
        self.przyciski_monety.append(przycisk_1)
        self.przyciski_monety.append(przycisk_2)
        self.przyciski_monety.append(przycisk_5)
        self.przyciski_monety.append(przycisk0)

        # ustalam położenie przycisków i ich rozciagniecie
        przycisk1.grid(row=2, column=0, padx=1, pady=1,sticky=W+S+E+N)
        przycisk2.grid(row=2, column=1, padx=1, pady=1,sticky=W+S+E+N)
        przycisk5.grid(row=2, column=2, padx=1, pady=1,sticky=W+S+E+N)

        przycisk10.grid(row=3, column=0, padx=1, pady=1,sticky=W+S+E+N)
        przycisk20.grid(row=3, column=1, padx=1, pady=1,sticky=W+S+E+N)
        przycisk50.grid(row=3, column=2, padx=1, pady=1,sticky=W+S+E+N)

        przycisk_1.grid(row=4, column=0, padx=1, pady=1,sticky=W+S+E+N)
        przycisk_2.grid(row=4, column=1, padx=1, pady=1,sticky=W+S+E+N)
        przycisk_5.grid(row=4, column=2, padx=1, pady=1,sticky=W+S+E+N)


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

        # dodaje przyciski do wyboru numeru produktu do zmiennej klasy Interfejs_automatu pinpad(listy)
        self.pinpad.append(przyc1)
        self.pinpad.append(przyc2)
        self.pinpad.append(przyc3)
        self.pinpad.append(przyc4)
        self.pinpad.append(przyc5)
        self.pinpad.append(przyc6)
        self.pinpad.append(przyc7)
        self.pinpad.append(przyc8)
        self.pinpad.append(przyc9)
        self.pinpad.append(przyc0)

        # ustalam położenie przycisków i ich rozciagniecie
        przyc1.grid(row=8, column=0, padx=1, pady=1,sticky=W+S+E+N)
        przyc2.grid(row=8, column=1, padx=1, pady=1,sticky=W+S+E+N)
        przyc3.grid(row=8, column=2, padx=1, pady=1,sticky=W+S+E+N)

        przyc4.grid(row=9, column=0, padx=1, pady=1,sticky=W+S+E+N)
        przyc5.grid(row=9, column=1, padx=1, pady=1,sticky=W+S+E+N)
        przyc6.grid(row=9, column=2, padx=1, pady=1,sticky=W+S+E+N)

        przyc7.grid(row=10, column=0, padx=1, pady=1,sticky=W+S+E+N)
        przyc8.grid(row=10, column=1, padx=1, pady=1,sticky=W+S+E+N)
        przyc9.grid(row=10, column=2, padx=1, pady=1,sticky=W+S+E+N)

        przyc0.grid(row=11, column=1, padx=1, pady=1,sticky=W+S+E+N)

        ety = Label(self.okno, text='Napoje')  # tworze etykiete z tytułem Napoje
        ety.grid(row=13, column=1, padx=5, pady=5)  # ustalam ułożenie etykiety
        ety.config(font=("Arial", 15, "italic"), foreground="white",
                   background='black')  # ustalam rodzaj czcionki i jej wielkość, kolor tła i czcionki

        # tworze etykiety z numerami produktow i ich nazwami
        ety1 = Label(self.okno, text='30:woda gazowana')
        ety2 = Label(self.okno, text='31:woda niegazowana')
        ety3 = Label(self.okno, text='32:sok pomarańczowy')
        ety4 = Label(self.okno, text='33:sok porzeczkowy')
        ety5 = Label(self.okno, text='34:sok jabłkowy')
        ety6 = Label(self.okno, text='35:mirinda')
        ety7 = Label(self.okno, text='36:pepsi')
        ety8 = Label(self.okno, text='37:pepsi light')
        ety9 = Label(self.okno, text='38:cola')
        ety10 = Label(self.okno, text='39:cola zero')
        ety11 = Label(self.okno, text='40:nestea brzoskwiniowe')
        ety12 = Label(self.okno, text='41:nestea cytrynowe')
        ety13 = Label(self.okno, text='42:nestea zielona herbata')
        ety14 = Label(self.okno, text='43:tymbark pomarańcza-mięta')
        ety15 = Label(self.okno, text='44:tymbark jabłko-brzoskwinia')
        ety16 = Label(self.okno, text='45:tymbark jabłko-wiśnia')
        ety17 = Label(self.okno, text='46:tymbark jabłko-kiwi')
        ety18 = Label(self.okno, text='47:sprite')
        ety19 = Label(self.okno, text='48:7up')
        ety20 = Label(self.okno, text='49:oranżada cytrynowa')
        ety21 = Label(self.okno, text='50:oranżada wiśniowa')

        # ustalam ułozennie etykiet i ich wyrowanie
        ety1.grid(row=14, column=0, padx=1, pady=1, sticky=W)
        ety2.grid(row=14, column=1, padx=1, pady=1, sticky=W)
        ety3.grid(row=14, column=2, padx=1, pady=1, sticky=W)
        ety4.grid(row=15, column=0, padx=1, pady=1, sticky=W)
        ety5.grid(row=15, column=1, padx=1, pady=1, sticky=W)
        ety6.grid(row=15, column=2, padx=1, pady=1, sticky=W)
        ety7.grid(row=16, column=0, padx=1, pady=1, sticky=W)
        ety8.grid(row=16, column=1, padx=1, pady=1, sticky=W)
        ety9.grid(row=16, column=2, padx=1, pady=1, sticky=W)
        ety10.grid(row=17, column=0, padx=1, pady=1, sticky=W)
        ety11.grid(row=17, column=1, padx=1, pady=1, sticky=W)
        ety12.grid(row=17, column=2, padx=1, pady=1, sticky=W)
        ety13.grid(row=18, column=0, padx=1, pady=1, sticky=W)
        ety14.grid(row=18, column=1, padx=1, pady=1, sticky=W)
        ety15.grid(row=18, column=2, padx=1, pady=1, sticky=W)
        ety16.grid(row=19, column=0, padx=1, pady=1, sticky=W)
        ety17.grid(row=19, column=1, padx=1, pady=1, sticky=W)
        ety18.grid(row=19, column=2, padx=1, pady=1, sticky=W)
        ety19.grid(row=20, column=0, padx=1, pady=1, sticky=W)
        ety20.grid(row=20, column=1, padx=1, pady=1, sticky=W)
        ety21.grid(row=20, column=2, padx=1, pady=1, sticky=W)

        # ustalam kolor tla, kolor,rodzaj i wielkosc czcionki w etykietach
        ety1.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety2.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety3.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety4.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety5.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety6.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety7.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety8.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety9.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety10.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety11.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety12.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety13.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety14.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety15.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety16.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety17.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety18.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety19.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety20.config(font=("Arial", 11, "italic"), foreground="white", background='black')
        ety21.config(font=("Arial", 11, "italic"), foreground="white", background='black')

    def run(self):
        self.okno.mainloop()#uruchamiam okno

    def zamknij(self,numer):
        self.okno.quit() #zamykam okno
        self.okno.destroy() #zwalniam zasoby zajete przez okno

    wrzucone=0
    def wrzucono_monete(self,moneta):
        self.przelacz_monety(False)#ustawiam stan przycisku DISABLED-wylaczony
        self.wpis0.delete(0, END)  # czyszcze pole wpis0
        self.wrzucone += moneta  # zwiekszam wartosc zmiennej wrzucone o wartosc monety
        self.wpis0.insert(0, self.wrzucone / 100)  # wprowadzam tekst do pola wpis0
        self.okno.update()  # przetwarzam okno
        time.sleep(1)
        automat.wrzucMonete(moneta) #wywoluje funkcje wrzucMonete z klasy Automat_z_napojami
        self.przelacz_monety(True)  # ustawiam stan przycisku na NORMAL-wlaczony

    def kliknieto_przycisk(self,numer):
        automat.wybierz(str(numer)) #wywoluje funkcje wybierz z klasy Automat_z_napojami

    przyciski_monety=[]#lista przysisków do wrzucania monet
    def przelacz_monety(self,wlacz_wylacz):
        for przycisk in self.przyciski_monety:
            if wlacz_wylacz==True:
                przycisk.config(state=NORMAL)#ustawiam stan przycisku na NORMAL-wlaczony
            else:
                przycisk.config(state=DISABLED)#ustawiam stan przycisku DISABLED-wylaczony

    pinpad=[]#lista przysisków do wyboru numeru kodu
    def przelacz_pinpad(self,wlacz_wylacz):
        for przycisk in self.pinpad:
            if wlacz_wylacz==True:
                przycisk.config(state=NORMAL)#ustawiam stan przycisku na NORMAL-wlaczony
            else:
                przycisk.config(state=DISABLED)#ustawiam stan przycisku na DISABLED-wylaczony

if __name__=="__main__":
    interfejs=Interfejs_automatu()
    interfejs.interfejs()
    interfejs.run()