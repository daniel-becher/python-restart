contacts = []


def add(kontakty):
    jmeno = input("Zadej jmeno: ")
    telefon = input("Zadej telefon: ")
    mail = input("Zadej mail: ")
    kontakty.append({"jmeno": jmeno, "telefon": telefon, "mail": mail})
    return kontakty


def show(kontakty):
    for kontakt in kontakty:
        for keys, values in kontakt.items():
            print(keys, "=", values)


def find(kontakty):
    name = input("Zadej hledané jméno: ")
    nalezeno = 0
    for contact in kontakty:
        if contact["jmeno"] == name:
            print(contact)
            nalezeno += 1

    if nalezeno == 0:
        print("Kontakt nenalezen.")


def delete(kontakty):
    name_to_delete = input("Zadej jméno které chceš odstranit: ")
    pocet_pred = len(kontakty)
    for name in kontakty[:]:
        if name["jmeno"] == name_to_delete:
            kontakty.remove(name)
    if len(kontakty) == pocet_pred:
        print("Kontakt nenalezen.")


def app():
    while True:
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


app()
