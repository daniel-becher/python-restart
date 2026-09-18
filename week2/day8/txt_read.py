radky = [
    "ahoj",
    "Jmenuji se Dan",
    "Jsem z Ostravy",
    "Hrál jsem hokej",
    "Uz ho nehraju",
]

with open("pokus.txt", "w", encoding="utf-8") as f:
    for radek in radky:
        f.write(radek + "\n")
with open("pokus.txt", "r", encoding="utf-8") as f:
    for cislo, radek in enumerate(f, start=1):
        print(cislo, radek.strip())
