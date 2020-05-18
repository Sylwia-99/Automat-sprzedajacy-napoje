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
Jednak test nr 7 wymagał czegoś innego. Musiałam więc delikatnie zmienić zamysł i podzielić metode wrzucMonete na wrzuc_monete i sprawdz_i_wydaj.
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
Więc nawet nie trzeba kompilować kodu, by sprawdzić, czy zadanie zostało zrealizowane. [Tutaj link, do szybszego sprawdzenia](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/bd7d65cca29d0ed8efa2ab0a9402c89cc1d21324/system_Automatu.py#L375-L463)
Na koniec, by delikatnie poprawić cały kod użyłam pylint i naniosłam poprawki, które ten mi wskazał.

## Linki do wymaganych w projeckie konstrukcji
### a. Lambda-wyrażenia: 
- [Użycie Eventu on_zwroc_reszte](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L371)
- [Użycie Eventu on_zmiana_kodu](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L372)
- [Użycie Eventu on_czekaj_na_pieniadze](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L373)
- [Użycie Eventu on_wydaj_produkt](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L374)
- [Użycie Eventu on_nie_ma_w_automacie](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L375)
- [Użycie Eventu on_blad](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L376)
- [Obsługa przycisków do wrzucania monet](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/interface_Automatu.py#L90-L108)
- [Obsługa przycisków do wyboru numeru produktu](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/interface_Automatu.py#L129-L148)
### b1. Dictionary comprehensions:
- [użycie do wyzerowania monet w schowku monety_do_wydania w metodzie zwroc_wartosc](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L45)
- [użycie do wyzerowania monet w schowku w metodzie sprawdz_i_wydaj](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/f9b232bc69610e9bcd4cd4cc2d1ad880faad1f64/system_Automatu.py#L300)
- [użycie do wyzerowania monet w schowku w metodzie przerwij](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L313)
- [użycie do tworzenia pustego schowka monety_w_schowku](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/system_Automatu.py#L249)
### b2.List comprehensions:
- [użycie do dodania przycisków do wrzucania monet do zmiennej klasy przyciski_monety(lista)](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/interface_Automatu.py#L113)
- [użycie do dodania przycisków do wyboru kodu do zmiennej klasy pinpad(lista)](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/interface_Automatu.py#L152)
### c. Klasy
- [Klasa realizująca funkcjonalność programu](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/f9b232bc69610e9bcd4cd4cc2d1ad880faad1f64/system_Automatu.py#L203)
- [Klasa odpowiedzialna za interfejs użytkownika](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/interface_Automatu.py#L7)
### d. Moduły
- [Import modułu system_Automatu do pliku interface_Automatu.py](https://github.com/Sylwia-99/Automat-sprzedajacy-napoje/blob/e2a0ecbff34f20c9810da7c278e32e2775c758c9/interface_Automatu.py#L3)
 

