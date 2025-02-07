# Ecrire un programme pour affichier Bonjour M. Ou Mme {Prenom} {Nom}

Nom = input(str("Quelle est votre nom ? "))
Prenom = input(str("Quelle est votre prenom ? "))

print (f"Bonjour M. Ou Mme {Prenom.capitalize()} {Nom.upper()}")