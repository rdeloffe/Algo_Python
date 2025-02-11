def Affiche(nom, prenom) :
    return nom, prenom

prenom = str(input("Quelle est votre prenom ? "))
nom = str(input("Quelle est votre nom ? "))

le_nom, le_prenom = Affiche(nom, prenom)
print(f"Vous vous appelez : {le_nom} {le_prenom}")
