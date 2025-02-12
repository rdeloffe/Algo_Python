import random

Instruction = int(input(
    "Taper le numéro du test que vous voulez faire :\n"
    "1. Vérification ADN\n"
    "2. Saisie d'ADN\n"
    "3. Comparaison entre ADN\n"
    "Votre choix : "
))


chaine_adn = str(input("Donnez une chaîne d'ADN : "))
sequance_adn = str(input("Donner une sequance d'ADN : "))

def verification_adn(chaine_adn) :
    count = 0
    for lettre in chaine_adn :
        if lettre not in {"a", "t", "c", "g"} :
            count += 1
            if count >= 1 :
                return False
    return True

true_false = verification_adn(chaine_adn)
if Instruction == 1 :
    print(f"La chaine {chaine_adn} est : {true_false}")

def saisie_adn(chaine_adn, true_false) : #pppp False
    if true_false == False : #good  
        chaine_adn = list(chaine_adn)#["p","p","p","p"]
        for lettres in range(len(chaine_adn)) : 
            if chaine_adn[lettres] not in {"a", "t", "c", "g"} : 
                chaine_adn[lettres] = random.choice(["a", "t", "c", "g"])
        return "".join(chaine_adn)
    return chaine_adn


if Instruction == 2 :
        new_chaine_adn = saisie_adn(chaine_adn, true_false)
        if chaine_adn != new_chaine_adn :
            print(f"Voici la nouvelle chaine d'ADN {new_chaine_adn}")


def proportion(chaine_adn, sequance_adn) :
    return chaine_adn.count(sequance_adn)


if Instruction == 3 :
    compter = proportion(chaine_adn,sequance_adn)
    print(f"Il y a {compter} adn identique")

