from fonction import *


chaine_adn = str(input("Donnez une chaîne d'ADN : "))
if Instruction == 3 :
    sequance_adn = str(input("Donner une sequance d'ADN : "))

true_false = verification_adn(chaine_adn)
if Instruction == 1 :
    print(f"La chaine {chaine_adn} est : {true_false}")

if Instruction == 2 :
        new_chaine_adn = saisie_adn(chaine_adn, true_false)
        if chaine_adn != new_chaine_adn :
            print(f"Voici la nouvelle chaine d'ADN {new_chaine_adn}")


if Instruction == 3:
    compter = proportion(chaine_adn, sequance_adn)
    print(f"Il y a {compter} lettres ADN identiques entre la séquence et la chaîne.")



