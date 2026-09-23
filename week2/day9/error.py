import json
from pathlib import Path


class NeplatnyKontakt(ValueError):
    pass


SOUBOR = Path("kontakty.json")


def load():
    try:
        with open(SOUBOR, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def zkontroluj_mail(mail):
    if "@" not in mail:
        raise NeplatnyKontakt(f"Email {mail} nema zavinac")


def zkontroluj_telefon(telefon):
    if not telefon.isdigit() or len(telefon) != 9:
        raise NeplatnyKontakt(f"Telefon {telefon} je spatne")


contacts = load()


def save(kontakty):
    with open(SOUBOR, "w", encoding="utf-8") as f:
        json.dump(kontakty, f, ensure_ascii=False, indent=2)


def add(kontakty):
    jmeno = input("Zadej jmeno: ").strip()
    telefon = input("Zadej telefon: ").replace(" ", "")
    mail = input("Zadej mail: ").strip()
    zkontroluj_telefon(telefon)
    zkontroluj_mail(mail)
    kontakty.append({"jmeno": jmeno, "telefon": telefon, "mail": mail})
    save(kontakty)
    return kontakty


def show(kontakty):
    for kontakt in kontakty:
        for keys, values in kontakt.items():
            print(keys, "=", values)


def find(kontakty):
    name = input("Zadej hledané jméno: ").strip()
    nalezeno = 0
    for contact in kontakty:
        if contact["jmeno"] == name:
            print(contact)
            nalezeno += 1

    if nalezeno == 0:
        print("Kontakt nenalezen.")


def delete(kontakty):
    name_to_delete = input("Zadej jméno které chceš odstranit: ").strip()
    pocet_pred = len(kontakty)
    for name in kontakty[:]:
        if name["jmeno"] == name_to_delete:
            kontakty.remove(name)
    if len(kontakty) == pocet_pred:
        print("Kontakt nenalezen.")
    save(kontakty)


def app():
    while True:
        try:
            choice = int(
                input(
                    "Stiskni 1 pro přidání nového kontaktu\nStiskni 2 pro zobrazení kontaktů\nStiskni 3 pro nalezení kontaktu podle jména\nStiskni 4 pro odebrání kontaktu\nStiskni 5 pro ukončení\n"
                )
            )
            if choice == 1:
                add(contacts)
            elif choice == 2:
                show(contacts)
            elif choice == 3:
                find(contacts)
            elif choice == 4:
                delete(contacts)
            elif choice == 5:
                break
            else:
                print("Zadej číslo od 1 do 5.")
        except NeplatnyKontakt as e:
            print(e)
        except ValueError:
            print("Zadej cislo od 1 do 5.")


app()
