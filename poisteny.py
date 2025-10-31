#poisteny.py → trieda Poisteny (iba dáta + toString)
class Poisteny:
    def __init__(self, meno: str, priezvisko: str, vek: int, telefon: str):
        if not meno.strip():
            raise ValueError("Meno nesmie byť prázdne.")
        if not priezvisko.strip():
            raise ValueError("Priezvisko nesmie byť prázdne.")
        self.meno = meno.strip()
        self.priezvisko = priezvisko.strip()
        self.vek = vek
        self.telefon = telefon.strip()

    def __str__(self):
        return f"{self.meno} {self.priezvisko}, vek: {self.vek}, tel: {self.telefon}"

