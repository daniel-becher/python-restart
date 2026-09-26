from models import zkontroluj_telefon, zkontroluj_mail


def add(uloziste, kontakty, jmeno, telefon, mail):
    telefon = telefon.replace(" ", "")
    zkontroluj_telefon(telefon)
    zkontroluj_mail(mail)
    kontakty.append({"jmeno": jmeno, "telefon": telefon, "mail": mail})
    uloziste.uloz(kontakty)
    return kontakty


def show(kontakty):
    for kontakt in kontakty:
        for keys, values in kontakt.items():
            print(keys, "=", values)


def find(kontakty, jmeno):
    nalezeno = 0
    for contact in kontakty:
        if contact["jmeno"] == jmeno:
            print(contact)
            nalezeno += 1

    if nalezeno == 0:
        print("Kontakt nenalezen.")


def delete(uloziste, kontakty, jmeno):
    pocet_pred = len(kontakty)
    for kontakt in kontakty[:]:
        if kontakt["jmeno"] == jmeno:
            kontakty.remove(kontakt)
    uloziste.uloz(kontakty)
    return len(kontakty) < pocet_pred

