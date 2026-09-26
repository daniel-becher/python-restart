from datetime import date, datetime, timedelta

dnes = date.today()
narozeniny = date(2001, 2, 10)
print((dnes - narozeniny).days, "dni zivota")
print(dnes + timedelta(days=30))
print(dnes.strftime("%d.%m.%Y"))