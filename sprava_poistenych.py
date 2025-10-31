#sprava_poistenych.py → trieda SpravaPoistenych (pridávanie, hľadanie, zoznam)

from poisteny import Poisteny

class SpravaPoistenych:
    def __init__(self):
        self.poisteni = []

    def pridaj_poisteneho(self, meno, priezvisko, vek, telefon):
        poisteny = Poisteny(meno, priezvisko, vek, telefon)
        self.poisteni.append(poisteny)

    def zobraz_vsetkych(self):
        return self.poisteni

    def najdi_poisteneho(self, meno, priezvisko):
        for p in self.poisteni:
            if p.meno.lower() == meno.lower() and p.priezvisko.lower() == priezvisko.lower():
                return p
        return None
