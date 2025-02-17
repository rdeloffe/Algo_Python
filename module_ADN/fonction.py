import random

Instruction = int(input(
    "Taper le numéro du test que vous voulez faire :\n"
    "1. Vérification ADN\n"
    "2. Saisie d'ADN\n"
    "3. Comparaison entre ADN\n"
    "Votre choix : "
))

def verification_adn(chaine_adn) :
    count = 0
    for lettre in chaine_adn :
        if lettre not in {"a", "t", "c", "g"} :
            count += 1
            if count >= 1 :
                return False
    return True

def saisie_adn(chaine_adn, true_false) : #pppp False
    if true_false == False : #good  
        chaine_adn = list(chaine_adn)#["p","p","p","p"]
        for lettres in range(len(chaine_adn)) : 
            if chaine_adn[lettres] not in {"a", "t", "c", "g"} : 
                chaine_adn[lettres] = random.choice(["a", "t", "c", "g"])
        return "".join(chaine_adn)
    return chaine_adn

def proportion(chaine_adn, sequence_adn):
    count = 0
    for lettre in sequence_adn:
        count += chaine_adn.count(lettre)
    return count