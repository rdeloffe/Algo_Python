# Liste [Pos.Nom , Pos.Nom ...]

# SI panne moteur le premier passe dernier (append [Pos.Nom] PUIS pop[Pos.Nom]

# SI passe_en_tete [1.DEL] [2.OPP] (pop liste(0) insert(1, i.DEL )

# SI sauve_honneur [AD.DEL] [D.OPP] (pop liste (-2) append [i.DEL] )

#SI tire_blaser pop(0)

#SI retour_innatendu insert(-1, Concu)

Menu = int(input("\n"
    "------------------- Bienvenue à la course de module de Tatooine -------------------\n\n"
    "Combien de personnes participe a cette course cette année ? :"))

liste_nom = []

for nb in range (1,Menu + 1) :
    demander_nom = (input(f"Donner moi le nom du joueur {nb} : "))
    while not demander_nom.isalpha():
        print("Erreur : Veuillez entrer un nom valide (lettres uniquement).")
        demander_nom = input(f"Redonner moi le nom du joueur {nb} : ").strip()
    liste_nom.append(f" {nb}.{demander_nom} ")
print (f"Classement avant le depart : {liste_nom}")

def panne_moteur(liste_nom) :
    liste_nom.append(liste_nom[0])
    liste_nom.pop(0)

    for i in range(len(liste_nom)) :
        nom = liste_nom[i].split(".")[1] #On prend [1.Raph] on separe ['1' , 'Raph'] et on prend [Raph]
        liste_nom[i] = f"{i + 1}.{nom}" #Affichage = [1.Raph]
    return liste_nom

liste_nom_PM = panne_moteur(liste_nom)
print(f"Classement apres une panne moteur : {liste_nom_PM}")

def passe_en_tete(liste_nom) :

    liste_nom.insert(0, liste_nom[1])
    liste_nom.pop(2)

    for i in range(len(liste_nom)) :
        nom = liste_nom[i].split(".")[1] #On prend [1.Raph] on separe ['1' , 'Raph'] et on prend [Raph]
        liste_nom[i] = f"{i + 1}.{nom}" #Affichage = [1.Raph]
    return liste_nom

liste_nom_PT = passe_en_tete(liste_nom)
print(f"Classement apres le passage en tete {liste_nom_PT}")


def sauve_honneur(liste_nom) :
    liste_nom.append(liste_nom[-2])
    liste_nom.pop(-3)

    for i in range(len(liste_nom)) :
        nom = liste_nom[i].split(".")[1] #On prend [1.Raph] on separe ['1' , 'Raph'] et on prend [Raph]
        liste_nom[i] = f"{i + 1}.{nom}" #Affichage = [1.Raph]
    return liste_nom

liste_nom_SH = sauve_honneur(liste_nom)
print(f"Classement apres le passage en tete {liste_nom_SH}")


# SI passe_en_tete [1.DEL] [2.OPP] (pop liste(0) insert(1, i.DEL )
#modifiant la liste passée en argument de manière à ce que le premier module passe
#deuxième et le deuxième premier.


