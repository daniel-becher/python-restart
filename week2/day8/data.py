import csv
import random

jmena = ["Anna", "Petr", "Eva", "Jan", "Lucie", "Tomas", "Marie", "Karel"]
mesta = ["Praha", "Brno", "Ostrava", "Plzen", "Olomouc"]

with open("data.csv", "w", encoding="utf-8", newline="") as f:
    zapisovac = csv.DictWriter(f, fieldnames=["jmeno", "vek", "mesto"])
    zapisovac.writeheader()

    for i in range(200):
        radek = {
            "jmeno": random.choice(jmena),
            "vek": random.randint(18, 70),
            "mesto": random.choice(mesta),
        }

        # do kazdeho desateho radku schvalne chyba
        if i % 10 == 0:
            radek["vek"] = random.choice(["", "dvacet", "-5"])
        if i % 25 == 0:
            radek["jmeno"] = ""

        zapisovac.writerow(radek)

print("Hotovo, 200 radku v data.csv")
