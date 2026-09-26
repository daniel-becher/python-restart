from dataclasses import dataclass


class NeplatnyKontakt(ValueError):
    pass


def zkontroluj_mail(mail):
    if "@" not in mail:
        raise NeplatnyKontakt(f"Email {mail} nema zavinac")


def zkontroluj_telefon(telefon):
    if not telefon.isdigit() or len(telefon) != 9:
        raise NeplatnyKontakt(f"Telefon {telefon} je spatne")


@dataclass
class Kontakt:
    jmeno: str
    telefon: str
    email: str

    def __post_init__(self):
        zkontroluj_telefon(self.telefon)
        zkontroluj_mail(self.email)


class FiremniKontakt(Kontakt):
    def __init__(self, jmeno, telefon, mail, ico):
        super().__init__(jmeno, telefon, mail)
        self.ico = ico


from datetime import date, timedelta, datetime


class OsobniKontakt(Kontakt):
    def __init__(self, jmeno, telefon, mail, datum_narozeni):
        super().__init__(jmeno, telefon, mail)
        try:
            self.datum_narozeni = datetime.strptime(datum_narozeni, "%d.%m.%Y").date()
        except ValueError:
            raise NeplatnyKontakt(f"Datum {datum_narozeni} je neplatne")


dnes = date.today()

bracha = OsobniKontakt("Ondra", "733733733", "@", "22.2.2004")
becks = OsobniKontakt("Ondra", "733733733", "@", "30.11.2004")
ja = OsobniKontakt("Dan", "733733733", "@", "10.2.2001")
simca = OsobniKontakt("Simca", "733733733", "@", "28.11.2005")
tatka = OsobniKontakt("Petr", "733733733", "@", "28.10.1972")
mamka = OsobniKontakt("Jana", "733733733", "@", "13.3.1973")


def narozeniny_v_roce(datum, rok):
    try:
        return datum.replace(year=rok)
    except ValueError:
        return datum.replace(year=rok, day=28)


def pocet_dni(kdo):
    narozeniny = narozeniny_v_roce(kdo.datum_narozeni, year=dnes.year)
    if narozeniny < dnes:
        narozeniny = narozeniny_v_roce(kdo.datum_narozeni, year=dnes.year + 1)
    return (narozeniny - dnes).days


# from collections import Counter, defaultdict
# print(Counter("programator"))
# print(Counter("programator").most_common(3))