popu_initial = int(input("Choisir le nombre d'habitant :"))

t = 0.1
popu_visee = int(input("Quelle population vous voulez au final :"))
annee = 0

if popu_initial >= popu_visee :
    print ("Pas possible faut unn nombre plus grand")
    exit()
else :
    while popu_initial < popu_visee :
        popu_initial = popu_initial * (1 + t)
        annee += 1
        print(f"Année {annee} : Votre population est de {popu_initial} personnes")

print(f"Il vous a fallu {annee} ans pour atteindre votre population visée qui est de {popu_visee} personnes ")
