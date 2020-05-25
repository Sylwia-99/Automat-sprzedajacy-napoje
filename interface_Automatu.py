from tkinter import Label, Tk, Entry, Button, messagebox, W, S, E, N, END, NORMAL, DISABLED
import time
import system_Automatu  # importuje moduł system_Automatu

automat = system_Automatu.AutomatZnapojami()  # wywoluje konsturktor głownej klasy systemu_Automatu

class InterfejsAutomatu:
    """
    klasa InterfejsAutomatu główna klasa Interfejsu Automatu
    Zmienne:
        okno-Tworzy główne okno Automatu.
        wpis0-Tworzy pole wyświetlające wrzucone monety.
        wpis-Tworzy pole wyświetlające wybrany numer napoju.
        wrzucone-Przechowuje wartosc wrzoconych monet tymczasowo.
        przyciski_monety- Przechowuje liste przycisków wrzucania monet.
        pinpad-Przechowuje liste przycisków do wyboru kodu.
    Metody:
        interfejs() dodaje etykiety, przyciski
        run() uruchamia interfes, czyli wszystkie elementy okna i samo okno będą zaladowane po jej wywołaniu.
        zamknij(numer) zamyka i niszczy okno głowne okno interfejsu.
        wrzucono_monete(moneta) Do obsługi przycisków, wrzucania monet, by dodawać wrzucone monety do schowka, wyświetlać sume wrzuconych monet.
        kliknieto_przycisk(numer) Uruchamia funkcję z klasy AutomatZnapojami(głównej klasy automatu) po kliknięciu odpowiedniego przycisku z numerem.
        przelacz_monety(wlacz_wylacz) Ustawia stan przycisków do wrzucania monet.
        przelacz_pinpad(wlacz_wylacz) Ustawia stan przycisków do wrzucania monet.
        na_informacje(info) Funkcja do przypisania numeru do kodu.
        na_kod(kod) Funkcja do wpisywania numeru produktu w polu po kliknieciu przycisków do wyboru produktów.
        wrzucanie_monet(kwota) Funkcja do wyświetlania informacji o cenie produktu, który został wybrany.
        zwrot_pieniedzy(monety) Funkcja do zwrotu pieniedzy gdy albo klikamy pzerwij, albo trzeba wydac reszte wyskakuje informacja o tym ile reszty zwrociliśmy.
        wydano_produkt(produkt) Funkcja do wyswietlania informacji o tym, jaki produkt został kupiony.
        przerwij() Funkcja do obsługi przycisku przerwij, by po jego kliknięciu automat oddawał wrzucone monet.
        nie_moze_wydac(self) Funkcja do wyświetlenia informacji o tym, że automat nie może wydac reszty i trzeba wrzucić wyliczoną kwote.
        nie_ma_w_automacie(self,produkt) Funkcja do wyswietlania informacji o tym, ze nie ma w automacie wybranego produktu.
    """
    def __init__(self):
        """
        Konstruktor klasy.
        """
        self.okno = Tk()  # towrze główne okno
        self.okno.resizable(width=True, height=True)  # pozwalam na rozciaganie okna
        self.okno.configure(background='black')  # ustalam tlo okna

        # tworze puste pole, ustawiam jego szerokosc, kolor tła i czcionki
        self.wpis0 = Entry(self.okno, width=30, background='silver', foreground='black')
        self.wpis0.grid(row=1, column=1, padx=1, pady=1)  # ustalam ułożenie i wielkosc pola

        # tworze puste pole, ustawiam jego szerokosc, kolor tła i czcionki
        self.wpis = Entry(self.okno, width=30, background='silver', foreground='black')
        self.wpis.grid(row=7, column=1, padx=1, pady=1)  # ustalam ułożenie i wielkosc pola

        self.wrzucone = 0
        self.przyciski_monety = []  # lista przysisków do wrzucania monet
        self.pinpad = []  # lista przysisków do wyboru numeru kodu

    def interfejs(self):
        """
        Funkcja tworzy etykiety obok pól, przyciski i określa obsługę kliknięcia przycisku.
        """
        # tworze główną etykiete z tytułem Aplikacji, ustalam kolor tla i czcionki
        etykieta1 = Label(self.okno, text='Automat z napojami',
                          foreground="white", background='black')
        etykieta1.grid(row=0, column=1, padx=5, pady=5, sticky=W+S+E+N)  # ustalam ułożenie etykiety
        etykieta1.config(font=("Arial", 16, "italic"))  # ustalam rodzaj czcionki i jej wielkość

        # tworze etykiete z tytułem Wrzucona kwota, ustalam kolor tla i czcionki
        etykieta2 = Label(self.okno, text='Wrzucona kwota',
                          foreground="white", background='black')
        etykieta2.grid(row=1, column=0, padx=1, pady=1, sticky=W+S+E+N)  # ustalam ułożenie etykiety
        etykieta2.config(font=("Arial", 13, "italic"))  # ustalam rodzaj czcionki i jej wielkość

        # tworze etykiete z tytułem Wybrany numer, ustalam kolor tla i czcionki
        etykieta3 = Label(self.okno, text='Wybrany numer', foreground="white", background='black')
        etykieta3.grid(row=7, column=0, padx=4, pady=4)  # ustalam ułożenie etykiety
        etykieta3.config(font=("Arial", 13, "italic"))  # ustalam rodzaj czcionki i jej wielkość

        # tworze przycisk Zamknij i ustalam obsługe jego kliknięcia
        przycisk = Button(self.okno, text="Zamknij", command=self.zamknij)
        przycisk.grid(row=22, column=2, padx=4, pady=4, sticky=E)  # ustalam ułożenie przycisku i jego wyrownanie
        przycisk.bind("<Button-1>", self.zamknij)  # ustalam,że przycisk reaguje na pliknięcie na niego myszką
        # ustalam rodzaj czcionki, wielkość oraz kolor przycisku i czcionki
        przycisk.config(font=("Arial", 10, "italic"), background="silver", foreground='red')

        # tworze przycisk Przerwij i ustalam obsługe jego kliknięcia
        przycisk0 = Button(self.okno, text="Przerwij", command=self.przerwij)
        przycisk0.grid(row=6, column=1, padx=4, pady=4)  # ustalam ułożenie przycisku
        przycisk0.bind("<Button-1>", self.przerwij)  # ustalam,że przycisk reaguje na pliknięcie na niego myszką
        # ustalam rodzaj czcionki i jej wielkość oraz kolor przycisku i czcionki
        przycisk0.config(font=("Arial", 12, "italic"),
                         foreground="black", background='silver')

        # tworze przyciski do wrzucania monet, ustalam obsługe ich kliknięcia, tytuł, rodzaj i wielkosc czcionki
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
        przyciski = \
            [przycisk1, przycisk2, przycisk5, przycisk10, przycisk20, przycisk50, przycisk_1, przycisk_2, przycisk_5]
        self.przyciski_monety = [n for n in przyciski]  # list comprehension

        # ustalam położenie przycisków i ich rozciagniecie
        przycisk1.grid(row=2, column=0, padx=1, pady=1, sticky=W+S+E+N)
        przycisk2.grid(row=2, column=1, padx=1, pady=1, sticky=W+S+E+N)
        przycisk5.grid(row=2, column=2, padx=1, pady=1, sticky=W+S+E+N)

        przycisk10.grid(row=3, column=0, padx=1, pady=1, sticky=W+S+E+N)
        przycisk20.grid(row=3, column=1, padx=1, pady=1, sticky=W+S+E+N)
        przycisk50.grid(row=3, column=2, padx=1, pady=1, sticky=W+S+E+N)

        przycisk_1.grid(row=4, column=0, padx=1, pady=1, sticky=W+S+E+N)
        przycisk_2.grid(row=4, column=1, padx=1, pady=1, sticky=W+S+E+N)
        przycisk_5.grid(row=4, column=2, padx=1, pady=1, sticky=W+S+E+N)

        # tworze przyciski do wyboru numeru produktu i ustalam obsługe ich kliknięcia, tytuł, rodzaj i rozmiar czcionki
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
        przyc = [przyc1, przyc2, przyc3, przyc4, przyc5, przyc6, przyc7, przyc8, przyc9, przyc0]
        self.pinpad = [n for n in przyc]  # list comprehension

        # ustalam położenie przycisków i ich rozciagniecie
        przyc1.grid(row=8, column=0, padx=1, pady=1, sticky=W+S+E+N)
        przyc2.grid(row=8, column=1, padx=1, pady=1, sticky=W+S+E+N)
        przyc3.grid(row=8, column=2, padx=1, pady=1, sticky=W+S+E+N)

        przyc4.grid(row=9, column=0, padx=1, pady=1, sticky=W+S+E+N)
        przyc5.grid(row=9, column=1, padx=1, pady=1, sticky=W+S+E+N)
        przyc6.grid(row=9, column=2, padx=1, pady=1, sticky=W+S+E+N)

        przyc7.grid(row=10, column=0, padx=1, pady=1, sticky=W+S+E+N)
        przyc8.grid(row=10, column=1, padx=1, pady=1, sticky=W+S+E+N)
        przyc9.grid(row=10, column=2, padx=1, pady=1, sticky=W+S+E+N)

        przyc0.grid(row=11, column=1, padx=1, pady=1, sticky=W+S+E+N)

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
        """
        Funkcja która uruchamia interfes, czyli wszystkie elementy okna i samo okno będą zaladowane po jej wywołaniu.
        """
        self.okno.mainloop()  # uruchamiam okno

    def zamknij(self, numer):
        """
        funkcja która uruchamia zamyka i niszczy okno głowne okno interfejsu
        """
        self.okno.quit()  # zamykam okno
        self.okno.destroy()  # zwalniam zasoby zajete przez okno

    def wrzucono_monete(self, moneta):
        """
        Funkcja do obsługi przycisków do wrzucania monet, by dodawać wrzucone monety do schowka, wyświetlać sume wrzuconych monet.
        :param moneta: Wartosc monety.
        """
        self.przelacz_monety(False)  # ustawiam stan przycisku DISABLED-wylaczony
        self.wpis0.delete(0, END)  # czyszcze pole wpis0
        self.wrzucone += moneta  # zwiekszam wartosc zmiennej wrzucone o wartosc monety
        self.wpis0.insert(0, self.wrzucone / 100)  # wprowadzam tekst do pola wpis0
        self.okno.update()  # przetwarzam okno
        time.sleep(1)
        automat.wrzuc_monete(moneta)  # wywoluje funkcje wrzucMonete z klasy Automat_z_napojami
        self.przelacz_monety(True)  # ustawiam stan przycisku na NORMAL-wlaczony

    def kliknieto_przycisk(self, numer):
        """
        Funkcja, która uruchamia funkcję z klasy Automat_z_napojami(głównej klasy automatu)
        po kliknięciu odpowiedniego przycisku z numerem
        :param numer: Numer produktu.
        """
        automat.wybierz(str(numer))   # wywoluje funkcje wybierz z klasy Automat_z_napojami

    def przelacz_monety(self, wlacz_wylacz):
        """
        Funkcja do ustawiania stanu przycisków do wrzucania monet.
        :param wlacz_wylacz: W zależności od jego wartości funkcja ustala, czy przycisk ma być włączony, czy wyłączony.
        """
        for przycisk in self.przyciski_monety:
            if wlacz_wylacz is True:
                przycisk.config(state=NORMAL)  # ustawiam stan przycisku na NORMAL-wlaczony
            else:
                przycisk.config(state=DISABLED)  # ustawiam stan przycisku DISABLED-wylaczony

    def przelacz_pinpad(self, wlacz_wylacz):
        """
        Funkcja do ustawiania stanu przycisków do wybierania numeru produktu.
        :param wlacz_wylacz: W zależności od jego wartości funkcja ustala, czy przycisk ma być włączony, czy wyłączony.
        """
        for przycisk in self.pinpad:
            if wlacz_wylacz is True:
                przycisk.config(state=NORMAL)  # ustawiam stan przycisku na NORMAL-wlaczony
            else:
                przycisk.config(state=DISABLED)  # ustawiam stan przycisku na DISABLED-wylaczony

    def na_informacje(self, info):
        """
        Funkcja do przypisania numeru do kodu.
        :param info: numer wybranego produktu
        """
        kod = str(info)
        self.wpis.delete(0, END)  # czyszcze pole wpis
        self.wpis.insert(0, kod)  # wprowadzam tekst do pola wpis
        self.okno.update()  # przetwarzam okno

        time.sleep(1)
        self.wpis.delete(0, END)  # czyszcze pole wpis
        self.przelacz_pinpad(True)  # ustawiam stan przycisku na NORMAL-wlaczony

    def na_kod(self, kod):
        """
        Funkcja do wpisywania numeru produktu w polu po kliknieciu przycisków do wyboru produktów.
        :param kod: Numer produktu.
        """
        kod = str(kod)
        self.wpis.delete(0, END)  # czyszcze pole wpis
        self.wpis.insert(0, kod)  # wprowadzam tekst do pola

    def wrzucanie_monet(self, kwota):
        """
        Funkcja do wyświetlania informacji o cenie produktu, który został wybrany.
        :param kwota: Cena produktu.
        """
        self.przelacz_pinpad(False)  # ustawiam stan przycisku DISABLED-wylaczony
        messagebox.showinfo("UWAGA", "Cena: " + str(kwota / 100) + "        WRZUC MONETY ")  # tworze nowe okienko, by wyświetlić informacje

    def zwrot_pieniedzy(self, monety):
        """
        Funkcja do zwrotu pieniedzy.

        Gdy albo klikamy pzerwij, albo trzeba wydac reszte wyskakuje informacja o tym ile reszty zwrociliśmy.
        :param monety: Wartość monety.
        """
        self.wrzucone = 0  # zeruje wartość wrzuconych monet
        for wartosc, ilosc in monety.items():
            if ilosc > 0:
                if wartosc < 100:
                    grzl = str(wartosc)+"gr"
                else:
                    grzl = str(wartosc//100) + "zl"
                self.wpis0.delete(0, END)  # czyszcze pole wpis0
                messagebox.showinfo("UWAGA", "WYDANO {} razy {}".format(ilosc, grzl))  # tworze nowe okienko, by wyświetlić informacje
                self.okno.update()  # przetwarzam okno
                time.sleep(1)
        self.wpis0.delete(0, END)  # czyszcze pole wpis0

    def wydano_produkt(self, produkt):
        """
        Funkcja do wyswietlania informacji o tym, jaki produkt został kupiony.
        :param produkt: Nazwa produktu.
        :return:
        """
        self.wrzucone = 0  # zeruje wartość wrzuconych monet
        messagebox.showinfo("UWAGA", "WYDANO PRODUKT "+produkt)  # tworze nowe okienko, by wyświetlić informacje
        self.wpis.delete(0, END)  # czyszcze pole wpis
        self.przelacz_pinpad(True)  # ustawiam stan przycisku na NORMAL-wlaczony
        self.wpis.delete(0, END)  # czyszcze pole wpis

    def przerwij(self, produkt):
        """
        Funkcja do obsługi przycisku przerwij, by po jego kliknięciu automat oddawał wrzucone monety.
        """
        self.wrzucone = 0
        self.przelacz_monety(False)  # ustawiam stan przycisku DISABLED-wylaczony
        self.przelacz_pinpad(False)  # ustawiam stan przycisku DISABLED-wylaczony
        automat.przerwij()  # wywoluje funkcje przerwij z klasy Automat_z_napojami
        self.przelacz_pinpad(True)  # ustawiam stan przycisku na NORMAL-wlaczony
        self.przelacz_monety(True)  # ustawiam stan przycisku na NORMAL-wlaczony
        self.wpis.delete(0, END)  # czyszcze pole wpis0

    def nie_moze_wydac(self):
        """
        Funkcja do wyświetlenia informacji o tym, że automat nie może wydac reszty i trzeba wrzucić wyliczoną kwote.
        """
        self.wrzucone = 0  # zeruje wartość wrzuconych monet
        messagebox.showinfo("UWAGA", "TYLKO ODLICZONA KWOTA")  # tworze nowe okienko, by wyświetlić informacje
        self.wpis.delete(0, END)  # czyszcze pole wpis
        self.przelacz_pinpad(False)  # ustawiam stan przycisku na DISABLED-wylaczony
        self.wpis.delete(0, END)  # czyszcze pole wpis

    def nie_ma_w_automacie(self, produkt):
        """
        Funkcja do wyswietlania informacji o tym, ze nie ma w automacie wybranego produktu.
        """
        messagebox.showinfo("UWAGA", "BRAK TOWARU W AUTOMACIE")  # tworze nowe okienko, by wyświetlić informacje
        self.wpis.delete(0, END)  # czyszcze pole wpis
        self.przelacz_pinpad(True)  # ustawiam stan przycisku na NORMAL-wlaczony
        self.wpis.delete(0, END)  # czyszcze pole wpis


if __name__ == "__main__":
    interfejs = InterfejsAutomatu()
    interfejs.interfejs()
    automat.on_blad(interfejs.na_informacje)
    automat.on_zmiana_kodu(interfejs.na_kod)
    automat.on_czekaj_na_pieniadze(interfejs.wrzucanie_monet)
    automat.on_zwroc_reszte(interfejs.zwrot_pieniedzy)
    automat.on_wydaj_produkt(interfejs.wydano_produkt)
    automat.on_nie_ma_w_automacie(interfejs.nie_ma_w_automacie)
    automat.on_tylko_odliczona_kwota(interfejs.nie_moze_wydac)
    interfejs.run()
