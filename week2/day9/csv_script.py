# Otestuj čtyři situace a u každé ať uživatel dostane srozumitelnou větu místo červeného výpisu:
# 1) soubor neexistuje (FileNotFoundError)
# 2) chybí očekávaný sloupec (KeyError)
# 3) v čísle je text (ValueError)
# 4) soubor je prázdný
# Červený výpis, který vidíš při pádu, se jmenuje traceback. Čte se odspodu: poslední řádek říká typ chyby, nad ním je řádek tvého kódu, kde nastala.

import csv


def pridej_duvod(duvody, text):
    if text not in duvody:
        duvody[text] = 1
    else:
        duvody[text] += 1


zpracovano = 0
dobre = []
duvody = {}
try:
    with open("data_x.csv", encoding="utf-8") as f:
        for radek in csv.DictReader(f):
            zpracovano += 1
            if not radek["jmeno"]:
                pridej_duvod(duvody, "chybi jmeno")
                continue

            if not radek["vek"]:
                pridej_duvod(duvody, "chybi vek")
                continue
            try:
                vek = int(radek["vek"])
            except ValueError:
                pridej_duvod(duvody, "vek neni zapsany cislem")
                continue

            if vek < 0 or vek > 100:
                pridej_duvod(duvody, "spatny vek")
                continue
            dobre.append(radek)

except FileNotFoundError:
    print("Soubor nenalezen")
except KeyError:
    print("Chybi sloupec")
except UnicodeDecodeError:
    print("Soubor neni v kodovani UTF-8.")

else:
    if zpracovano == 0:
        print("Soubor neobsahuje zadna data.")
    else:
        print(f"Zpracovano: {zpracovano}")
        print(f"Zapsano:    {len(dobre)}")
        print(f"Vyhozeno:   {sum(duvody.values())}")
        for duvod, pocet in duvody.items():
            print(f"  - {duvod}: {pocet}")

        with open("data_clean.csv", "w", encoding="utf-8", newline="") as f:
            zapisovac = csv.DictWriter(f, fieldnames=["jmeno", "vek", "mesto"])
            zapisovac.writeheader()
            zapisovac.writerows(dobre)
