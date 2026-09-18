import csv


def pridej_duvod(duvody, text):
    if text not in duvody:
        duvody[text] = 1
    else:
        duvody[text] += 1


zpracovano = 0
dobre = []
duvody = {}

with open("data.csv", encoding="utf-8") as f:
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


print(f"Zpracovano: {zpracovano}")
print(f"Zapsano:    {len(dobre)}")
print(f"Vyhozeno:   {sum(duvody.values())}")
for duvod, pocet in duvody.items():
    print(f"  - {duvod}: {pocet}")

with open("data_clean.csv", "w", encoding="utf-8", newline="") as f:
    zapisovac = csv.DictWriter(f, fieldnames=["jmeno", "vek", "mesto"])
    zapisovac.writeheader()
    zapisovac.writerows(dobre)
