import argparse

parser = argparse.ArgumentParser(description="Správce poznámek")
sub = parser.add_subparsers(dest="prikaz", required=True)

p_pridej = sub.add_parser("pridej", help="Přidá poznámku")
p_pridej.add_argument("--text", required=True)
p_pridej.add_argument("-p", "--priorita", default="normalni")

p_seznam = sub.add_parser("seznam", help="Vypíše poznámky")

args = parser.parse_args()
print(args)
