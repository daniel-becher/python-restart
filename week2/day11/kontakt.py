class Kontakt:
    def __init__(self, jmeno, telefon, mail):
        self.jmeno = jmeno
        self.telefon = telefon
        self.mail = mail

    def je_mobil(self):
        return self.telefon.startswith(("6", "7"))

    def vypis(self):
        return f"{self.jmeno}, {self.telefon}, {self.mail}"


k = Kontakt("Danny", "777123456", "bechi@gmail.com")
print(k.jmeno, k.je_mobil())
print(k.vypis())
