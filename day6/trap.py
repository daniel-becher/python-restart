def pridej(polozka, do=None):
    if do is None:
        do = []
    do.append(polozka)
    return do


print(pridej("a"))
print(pridej("b"))
print(pridej("c"))
print(pridej("x", ["a"]) )

# Chápu proč to dělalo jak to dělalo. prostě se při každém použítí funkce přidej do listu přidalo jedno písmeno, které tam zůstalo. Po úpravě je To vždy none a změní se to na list při každém volání, takže to funguje správně.
