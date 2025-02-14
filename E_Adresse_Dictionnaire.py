#Stocker les adresses dans une liste 



all_adresses = []

# Adresse = {
#         "Ville" : "",
#         "Intitule voie" : "",
#         "Complement" : "",
#         "Numero" : "",
#         "CP" : ""
#         }

def ajout_adresse() :
    nb_adresse = int(input("Combien d'adresse voulez vous ajouter : "))
    print("\n")
    for nb in range (1,nb_adresse + 1) :
        ville = input("Entrer votre ville : ")
        voie = input("Entrer votre rue : ")
        complement = input("Entrer le complement (facultatif) : ")
        numero = input("Entrer le numero de la voie : ")
        cp = input("Entrer le code postal :")
        print("\n")
        newadresse = {
            "Ville" : ville,
            "Intitule voie" : voie,
            "Complement" : complement,
            "Numero" : numero,
            "CP" : cp
        }
        all_adresses.append(newadresse)
        print("Adresse bien enregistrer")

def afficher_adresse(all_adresses):
    for i, adresse in enumerate(all_adresses, 1):
        print(f"\n Adresse n°{i} \n")
        for cle, valeur in adresse.items():
            print(f"{cle} : {valeur}")


def editer_adresse(all_adresses) : 
    for i, adresse in enumerate(all_adresses, 1):
        print(f"\n Adresse n°{i} \n")
        for cle, valeur in adresse.items():
            print(f"{cle} : {valeur}")
    modif = int(input(f"Il y a {i} adresse. Quelle adresse voulez vous modifier ? "))
    while modif > i :
        print(f"Il y a que {i} adresse")
        modif = int(input(f"Il y a {i} adresse. Quelle adresse voulez vous modifier ? "))
        #################################################
        #A partir de la il faut faire en sorte que si on prend l'adresse 1 ça prends l'index zero
        #A l'affichage Adresse = 1 et non 0 avec les adresses de la 1 pas la 2
    for j in range(i):#Changer pour commencer a 1
        print(f"\n Adresse n°{j} \n")#Changer pour Adresse 1
        for cle, valeur in adresse.items():
            print(f"{cle} : {valeur}")
        
    modif_adresse = int(input("Que voulait vous changer (1.Ville / 2.Voie / 3.Complement / 4.Numero / 5.CP) ? "))
        
    match modif_adresse :
        case 1 :
            ville = input("Quelle est le nouveau nom de la ville ? ")
            all_adresses[modif]["Ville"] = ville
            print(f"Modification de la ville : {ville} ENREGISTRER")
            print("\n")
            for modif in all_adresses:
                print(f"\n Adresse n°{modif} \n")
                for cle, valeur in adresse.items():
                    print(f"{cle} : {valeur}")
        
    


while True :
    Menu = int(input("Choix : 1 , 2 , 3 , 4: "))
    match Menu :
        case 1 :
            ajout_adresse(),
        case 2 :
            afficher_adresse(all_adresses)
            if all_adresses == [] :
                print("Aucune adresse inscrit")
        case 3 :
            if all_adresses == [] :
                print("Aucune adresse inscrit")
            else :
                editer_adresse(all_adresses)
        case 4 :
            print("Au revoir")
            break

