# Kantor API NBP

Prosty kalkulator walutowy działający w terminalu. Skrypt łączy się z publicznym API Narodowego Banku Polskiego, pobiera aktualne kursy i pozwala na przeliczanie PLN na wybrane waluty obce (oraz odwrotnie).
Projekt napisany w celu praktycznego przećwiczenia zapytań HTTP i pracy z formatem JSON.

## Użyte technologie
* Python 
* `requests` 
* `json`

## Jak uruchomić lokalnie

Skopiuj poniższe komendy do terminala:
- git clone https://github.com/xjrkkk/Kantor.git
- cd Kantor
- pip install requests
- python kantor.py

### Główne wnioski z projektu
Mój pierwszy kod integrujący z zewnętrznym API. Najwięcej czasu zajęło mi zrozumienie, jak czytać słowniki i listy, które zwraca serwer NBP. Dodałem też podstawową obsługę wyjątków (try/except), żeby program nie "wywalał" się do systemu, gdy straci połączenie z siecią lub użytkownik wpisze złą wartość.
