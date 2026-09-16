lide = [
    {"jmeno": "Anna", "oddeleni": "IT", "plat": 60000},
    {"jmeno": "Petr", "oddeleni": "IT", "plat": 55000},
    {"jmeno": "Eva", "oddeleni": "HR", "plat": 48000},
]

celkem = 0
nejvyssi = 0
sum_it = 0
sum_hr = 0

for clovek in lide:
    celkem += clovek["plat"]

    if clovek["plat"] > nejvyssi:
        nejvyssi = clovek["plat"]
        highest = clovek["jmeno"]

    if clovek["oddeleni"] == "IT":
        sum_it += clovek["plat"]

    if clovek["oddeleni"] == "HR":
        sum_hr += clovek["plat"]

print(highest)
print(round(celkem / len(clovek), 2))
print(f"IT: {sum_it}")
print(f"HR: {sum_hr}")
