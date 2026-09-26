#CZK = int(input("Jaka je castka v CZK?: "))

#EUR = CZK / 25
#GBP = CZK / 28
#USD = CZK / 22

#print(
#    f"{'CZK':<5}{CZK:>10.2f}\n{'EUR':<5}{EUR:>10.2f}\n{'GBP':<5}{GBP:>10.2f}\n{'USD':<5}{USD:>10.2f}"
#)


s = "jan.novak@firma.cz"

# print(s.upper())
# print(s.replace(".","*"))
# print(s.split("@"))
# print(len(s))

print(s[0:9].replace("."," ").title().split("@"))