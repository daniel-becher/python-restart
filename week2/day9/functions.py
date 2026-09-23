def division(a, b):
    if b == 0:
        return "Nemuzes delit nulou!"
    else:
        return a / b


def bezpecne_deleni(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "You can't divide by zero!"


def safe_division(a, b):
    if b == 0:
        return None
    else:
        return a / b


vysledek = division(6, 0)
print(vysledek * 2)
