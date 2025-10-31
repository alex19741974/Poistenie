# app.py → konzolová logika (komunikácia s používateľom)
from sprava_poistenych import SpravaPoistenych

def nacitaj_text(popis):
    text = input(popis).strip()
    while not text:
        print("Hodnota nesmie byť prázdna.")
        text = input(popis).strip()
    return text

def main():
    sprava = SpravaPoistenych()

    while True:
        print("\n--- Evidencia poistných udalostí ---")
        print("1 - Pridať poisteného")
        print("2 - Zobraziť všetkých poistených")
        print("3 - Vyhľadať poisteného")
        print("4 - Koniec")

        volba = input("Zvoľ možnosť: ")

        if volba == "1":
            meno = nacitaj_text("Zadaj meno: ")
            priezvisko = nacitaj_text("Zadaj priezvisko: ")
            vek = int(nacitaj_text("Zadaj vek: "))
            telefon = nacitaj_text("Zadaj telefónne číslo: ")

            sprava.pridaj_poisteneho(meno, priezvisko, vek, telefon)
            print("Poistený bol pridaný.")

        elif volba == "2":
            poisteni = sprava.zobraz_vsetkych()
            if not poisteni:
                print("Zatiaľ nie sú evidovaní žiadni poistení.")
            else:
                for p in poisteni:
                    print(p)

        elif volba == "3":
            meno = nacitaj_text("Zadaj meno: ")
            priezvisko = nacitaj_text("Zadaj priezvisko: ")
            poisteny = sprava.najdi_poisteneho(meno, priezvisko)
            if poisteny:
                print("Nájdený poistený:")
                print(poisteny)
            else:
                print("Poistený sa nenašiel.")

        elif volba == "4":
            print("Koniec programu.")
            break

        else:
            print("Neplatná voľba.")

if __name__ == "__main__":
    main()

