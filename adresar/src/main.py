from cli import add, show, delete, find
from storage import JsonUloziste
import argparse
from models import NeplatnyKontakt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Adresář kontaktů")
    sub = parser.add_subparsers(dest="prikaz", required=True)

    p_pridej = sub.add_parser("pridej", help="Přidá kontakt")
    p_pridej.add_argument("--jmeno", required=True)
    p_pridej.add_argument("--telefon", required=True)
    p_pridej.add_argument("--mail", required=True)

    p_seznam = sub.add_parser("seznam", help="Vypíše seznam kontaktů")

    p_smaz = sub.add_parser("smaz", help="Smaže kontakt")
    p_smaz.add_argument("jmeno")

    p_najdi = sub.add_parser("najdi", help="Najde kontakt")
    p_najdi.add_argument("jmeno")

    args = parser.parse_args()

    uloziste = JsonUloziste("kontakty.json")
    kontakty = uloziste.nacti()

    try:
        if args.prikaz == "pridej":
            add(uloziste, kontakty, args.jmeno, args.telefon, args.mail)
            print(f"Kontakt {args.jmeno} přidán.")
        elif args.prikaz == "najdi":
            find(kontakty, args.jmeno)
        elif args.prikaz == "smaz":
            if delete(uloziste, kontakty, args.jmeno):
                print(f"Kontakt {args.jmeno} smazán.")
            else:
                print("Kontakt nenalezen.")
        elif args.prikaz == "seznam":
            show(kontakty)
    except NeplatnyKontakt as e:
        print(e)
