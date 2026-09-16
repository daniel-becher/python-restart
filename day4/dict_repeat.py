clovek = {"jmeno": "Danny", "vek": 25}
clovek["mesto"] = "Praha"
# print(clovek.get("mesto"))
clovek["mail"] = "bechi102@gmail.com"
clovek["country"] = "CZ"

# for klic, hodnota in clovek.items():
#     print(klic, "=", hodnota)

clovek["mesto"] = "klimkovice"
del clovek["country"]

# for klic, hodnota in clovek.items():
#     print(klic, "=", hodnota)

print(clovek)
