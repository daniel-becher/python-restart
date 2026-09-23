import random

random_number = random.randint(1, 100)
attempts = 0


def nacti_tip():
    while True:
        try:
            return int(input("Zadej cislo: "))
        except ValueError:
            print("To neni cislo! ")


def vyhodnot(tip, tajne):
    if tajne > tip:
        print("Tajné číslo je vyšší")
        return False
    elif tajne < tip:
        print("Tajné číslo je nižší")
        return False
    else:
        print("trefa")
        return True


def hraj():
    for _ in range(7):
        if vyhodnot(nacti_tip(), random_number):
            break
    else:
        print(f"Prohrál jsi, číslo bylo {random_number}")


hraj()
