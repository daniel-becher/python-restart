import json
from abc import ABC, abstractmethod

class Uloziste(ABC):
    
    @abstractmethod
    def nacti(self):
        pass

    @abstractmethod
    def uloz(self, kontakty):
        pass


class JsonUloziste(Uloziste):
    def __init__(self, cesta):
        self.cesta = cesta

    def nacti(self):
        try:
            with open(self.cesta, encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def uloz(self, kontakty):
        with open(self.cesta, "w", encoding="utf-8") as f:
            json.dump(kontakty, f, ensure_ascii=False, indent=2)


class PametoveUloziste(Uloziste):
    def __init__(self):
        self.data = []

    def nacti(self):
        return self.data

    def uloz(self, kontakty):
        self.data = kontakty
