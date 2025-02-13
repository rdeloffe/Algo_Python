mon_dict = {}

mon_dict = {
    "Clé 1" : "Valeur 1",
    2 : 1,
    True : False
}

#Pour acceder a une valeur liee a une clé
print(f"Valeur contenue a la clé 1 : {mon_dict['Clé 1']}")

#On re affecte la valeur de la clé
mon_dict["Clé 1"] = "Toto"
print(f"Valeur contenue a la clé 1 : {mon_dict['Clé 1']}")

#Ajouter un element 
print(mon_dict)
mon_dict["Clé 2"] = "casque"
print(mon_dict)

#Supprimer un element 
del mon_dict["Clé 2"] 
print(mon_dict)

mon_dict.pop(True)
print(mon_dict)
"\n"
#Supprime et renvoie l'element sous forme de tupe 
recup = mon_dict.popitem() #Seulement le dernier de la liste
print(mon_dict)
print(recup)

#Fusion de dictionnaire
personne = {
    "prenom" : "Christophe",
    "Nom" : "Toto", 
    "Age" : None
}
print("\n")
print(personne)
personne.update(mon_dict)
print(personne)

for cle, valeur in personne.items():
    print(f"ma clé:{cle} , et la valeur qui va avec {valeur}")

toto = {
    "Prenom" : "toto",
    "nom" : "tutu",
    "age" : 1
}

tata = {
    "Prenom" : "oui",
    "nom" : "non",
    "age" : 78
}

titi = {
    "Prenom" : "LAAAAAA",
    "nom" : "OOOOOOOO",
    "age" : 45
}

annuaire = [toto,tata,titi]
print(annuaire)
print("\n")
for personne in annuaire:
    print(f"personne n° {annuaire.index(personne)} qui s'appelle {personne['Prenom']}\n")
    for cle, valeur in personne.items():
        print(f"{cle} : {valeur}")