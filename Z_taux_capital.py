C = float(input("Quelle est votre capital ? "))
capital_initial = C
annee = 0
t = 0.4

while C < capital_initial * 2:
    C = C * (1 + t)
    annee += 1
    print(f"Année {annee} : Votre capital est de {C}€")

print(f"Il vous a fallu {annee} ans pour doubler votre capital qui est de {C}€")
