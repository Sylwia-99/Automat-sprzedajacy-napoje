# Raport
## Przygotowanie do projektu
Jako srodowisko wybrałam **PyCharm**, ponieważ dobrze mi się w nim pracuje.
Biblioteką graficzną, którą wybrałam był **Tkinter** polecony przez prowadzącego zajęcia. 
Dokumentacja nie do końca spełniała moje oczekiwania, ale dzięki paru instruktarzom na YT myśle, że poradziłam 
sobie całkiem nieźle.

## Budowa
Podzieliłam projekt na główny plik-interface_Automatu, w którym zajmuję się logiką interfacu tego Automatu. Interface posiada metody potrzebne w razie testów opisanych w projekcie. 
Między innymi obsługi przycisków przerwij (opisany w projekcie) i dodatkowo zamknij(który zamyka okno i zwalnia zajęte przez niego zasoby).
Dzięki messagebox wyswietlają się też potrzebne okienka, na przykład z informacją o wydawaniu reszty, o tym jaki produkt wybraliśmy i ile on kosztuje.
Oraz moduł- system_Automatu, który zawiera główną logikę Automatu.(Dzięki klasie PojemnikMonet przechowuje monety: nominały i ich ilości. 
Metody, które są w niej zawarte dodają monety do pojemnika oraz zwracają resztę. Natomiast dzięki klasie PojemnikProduktow przechowuje produkty: ich nazwy i numery. 
Metody znajdujące się w niej pozwalają na sprawdzenie ceny, nazwy, sprawdzenie czy produkt jest w Automacie oraz gdy przy zakupie zostanie kupiony dany produkt przyda się metoda 
zmniejsziwypisz. Przydatną klasą jest też WyborKodu, dzięki której możemy wybrać numer kodu(napoju), który chcemy kupić).

## Napotkane problemy
Problemy przysporzyła mi realizacja testów, bowiem na początku mój program miał wyrzucać od razu pieniądze wrzucone do pojemnika na Monety, jeśli wcześniej nie było wybranego kodu.
Jednak test nr 7 wymagał czegoś innego. Musiałam więc delikatnie zmienić zamysł i podzielić metode wrzucMonete na wrzucMonete i SprawdzIWydaj.
Początkowo nie mogłam sobie też poradzić z komunikatem Tylko Odliczona Kwota, gdyż pojawiał się nawet, gdy reszta była wydawana. Jednak z tym też uporałam sie w miarę szybko.

## Główne założenia
Chiałam zrealizować automat z napojami opisany w pliku Opis_Automat_sprzedajacy_napoje.md realizujący zadania podobne do Automatów, z których każdy z nas korzysta na codzień.
Dzięki wybraniu (z spisu produktów dostępnych w automacie) produktu i wrzuceniu odpowiednich monet każdy może kupić napój, na który ma ochotę. 

## Co udało się zrealizować
Myślę, że zrealizowałam wszystko, co potrzebne. Automat pozwala na wybranie kodu, zapłate i cieszenie się pysznymi napojami. Gdy niestety napoju nie ma w automacie(wpisany zły kod)
lub asortyment jest wykupiony dostajemy informację o braku produktu w automacie. Kiedy już zdecydujemy się na dany napój, wrzucimy pieniądze, ale najdzie nas ochota na coś innego,
to nie wszystko stracone, ponieważ istnieje przycisk przerwij, ktory pozwala na przerwanie transakcji i oddanie nam wrzuconej już kwoty. Kolory ustawione na automacie
są czarno białe. Czarne tło i napisy w kolorze białym niedość, że nie męczą tak oczu, jak odwrotna postać kolorystyczna to cieszą oczy osobom kochającym czerń(mi na pewno).
Testy, które powinny zostać przeprowadzone są udokumentowane w pliku system_Automatu na samym dole. W komentarzach mamy wyniki testów. 
Więc nawet nie trzeba kompilować kodu, by sprawdzić, czy zadanie zostało zrealizowane. [Tutaj link, do szybszego sprawdzenia](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/beb994f96405f62219eaf5e3747a128ba1775786/system_Automatu.py#L375-L463)

## Linki do wymaganych w projeckie konstrukcji
### a. Lambda-wyrażenia: 
- [Użycie Eventu onZwrocReszte](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L369)
- [Użycie Eventu onZmianaKodu](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L370)
- [Użycie Eventu onCzekajNaPieniadze](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L371)
- [Użycie Eventu onWydajProdukt](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L372)
- [Użycie Eventu onNiemaWAautomacie](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L373)
- [Użycie Eventu onBlad](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L374)
- [Obsługa przycisków do wrzucania monet](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/bd7d65cca29d0ed8efa2ab0a9402c89cc1d21324/interface_Automatu.py#L82-L99)
- [Obsługa przycisków do wyboru numeru produktu](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/bd7d65cca29d0ed8efa2ab0a9402c89cc1d21324/interface_Automatu.py#L128-L147)
### b1. Dictionary comprehensions:
- [użycie do wyzerowania monet w schowku MonetyDoWydania w metodzie zwrocWartosc](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L42)
- [użycie do wyzerowania monet w schowku w metodzie sprawdzIWydaj](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L297)
- [użycie do wyzerowania monet w schowku w metodzie przerwij](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L310)
- [użycie do tworzenia pustego schowka MonetyWSchowku](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L247)
### b2.List comprehensions:
- [użycie do dodania przycisków do wrzucania monet do zmiennej klasy przyciski_monety(lista)](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/interface_Automatu.py#L103)
- [użycie do dodania przycisków do wyboru kodu do zmiennej klasy pinpad(lista)](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/interface_Automatu.py#L143)
### c. Klasy
- [Klasa realizująca funkcjonalność programu](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/system_Automatu.py#L199)
- [Klasa odpowiedzialna za interfejs użytkownika](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/interface_Automatu.py#L6)
### d. Moduły
- [Import modułu system_Automatu do pliku interface_Automatu.py](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/3af016bf4ea84d80cf45e79e98e9ad2740e4448e/interface_Automatu.py#L1)
 

