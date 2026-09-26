Funkce má vracet None spíše než text. Ať funkce vždy dostane co má dostat. Ne jednou text, jednou číslo. 
pokud se chyba očekává, používá se if. try se používá, pokud je chyba vzácná. 

class se dá udělat tak, že před ní napíšeme @dataclass a from dataclasses import dataclass a pak nemusíme má vlastní innit i repr, ale nevyplatí se to když má class hodně vlastní logiky a valdiátorů. pak
se dá přidat __post_innit__ ve formátu
def __post_init__(self):
        zkontroluj_telefon(self.telefon)


parser.add_argument("--pocet", type=int, default=10)
parser.add_argument("--jmeno", required=True)
parser.add_argument("--stav", choices=["novy", "hotovo"])
parser.add_argument("--pocet", type=int, help="Kolik poznámek vypsat")
python poznamky.py mleko --vse        # args.vse = True



