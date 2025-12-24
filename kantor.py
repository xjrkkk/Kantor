import os
import requests    # terminal: pip install request
def wybor_waluty():
    while True: 
        print(30 * "-")
        print("1.Dolar amerykanski (USD)")
        print("2.Dolar australijsi (AUD)")
        print("3.Dolar kanadyjski (CAD)")
        print("4.EURO (EUR)")
        print("5.Forint (HUF)")
        print("6.Frank szwajcarski (CHF)")
        print("7.Funt brytyjski (GBP)")
        print("8.Jen japonski (JPY)")
        print("9.Korona czeska (CZK)")
        print("10.Korona dunska (DKK)")
        print("11.Korona norweska (NOK)")
        print("12.Korona szwedzka (SEK)")
        print("X.Wyjscie")
        print(30 * "-")
        waluta = input("Wybierz walute: ")
        wybor = {
            "1": "usd",
            "2": "aud",
            "3": "cad",
            "4": "eur",
            "5": "huf",
            "6": "chf",
            "7": "gbp",
            "8": "jpy",
            "9": "czk",
            "10": "dkk",
            "11": "nok",
            "12": "sek"
        }
        if waluta in wybor:
            wybrany_kod = wybor[waluta]
            url = f"https://api.nbp.pl/api/exchangerates/rates/c/{wybrany_kod}"
            response = requests.get(url)
            if response.status_code == 200:
                dane = response.json()
                bid = dane['rates'][0]['bid']
                ask = dane['rates'][0]['ask']
                kod = dane['code']
                print(f"✅ Pobrano aktualne kursy {kod}: kupno {bid}, sprzedaz {ask}")
                return bid, ask, kod
            else:
                print(f"❌ Błąd połączenia ")
                exit()            
        if waluta == "X":
            decyzja = input("Czy chcesz wyjsc? (t/n): ")
            if decyzja == 't':
                print("Wylogowano")
                exit()
            else:
                continue
        else:
            print("Nieznana opcja")
def kupno(kurs_kupna, kod):
    print(f"💰 KUPNO (Kurs: {kurs_kupna})")
    while True:
        try:
            waluta = float(input(f"Podaj ile chcesz wymienic {kod} "))
            if waluta <= 0:
                print("Podana kwota nie moze byc mniejsza badz rowna 0")
                continue
            zlotowki = waluta * kurs_kupna
            print(f"💵 Otrzymujesz {zlotowki:.2f} PLN")
            return  
        except ValueError:
            print("❌ Blad. Wpisz cyfry")
def sprzedaz(kurs_sprzedazy, kod):
    print(f"💰 SPRZEDAZ (Kurs: {kurs_sprzedazy})")
    while True:
        try:
            zlotowki = float(input("Podaj ile chcesz wymienic PLN "))
            if zlotowki <= 0:
                print("Podana kwota nie moze byc mniejsza badz rowna 0")
                continue
            waluta = zlotowki / kurs_sprzedazy
            print(f"💵 Otrzymujesz {waluta:.2f} {kod} ")
            return  
        except ValueError:
            print("❌ Blad. Wpisz cyfry")

def main():
    os.system('cls')
    print("💵 KANTOR WALUTOWY ONLINE 💵")
    while True:
        kurs_kupna, kurs_sprzedazy,kod = wybor_waluty()
        while True:
            
            print(40 * "-")
            print(f"1. Kupno ({kod} -> PLN)")
            print(f"2. Sprzedaz (PLN -> {kod})")
            print("3. Wroc do wyboru waluty ")
            print(40 * "-")

            wybor = input("Wybierz opcje: ")
            match wybor:
                case "1":
                    kupno(kurs_kupna, kod)
                case "2":
                    sprzedaz(kurs_sprzedazy,kod)
                case "3":
                    break
                case _:
                    print("Nieznana opcja")
main()