x = """Tohle je klasické cvičení na slovník. Postup: projdi text po znacích cyklem for znak in text:, a pro každý znak zvyš jeho počet ve slovníku.
Past: při prvním výskytu klíč ve slovníku ještě není. Řeší se tím, že se nejdřív zeptáš, jestli tam je, nebo použiješ pocty.get(znak, 0) + 1, což vrátí nulu, když klíč chybí.
Až to funguje, vypiš pět nejčastějších znaků. Na seřazení podle hodnoty použij sorted(pocty.items(), key=lambda x: x[1], reverse=True) a nelam si zatím hlavu s tím, co je lambda — jen si poznač, že se na to zeptáš později."""

dictionary = {}
for word in x:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0:5])
