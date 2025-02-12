import random

chaine_adn = str(input("Donnez une chaîne d'ADN : "))
sequance_adn = str(input("Donner une sequance d'ADN : "))

def verification_adn(sequance_adn) :
    count = 0
    for lettre in chaine_adn :
        if lettre not in sequance_adn :
            count += 1
            if count >= 1 :
                return False
    return True


true_false = verification_adn(sequance_adn)
print(f"La chaine {chaine_adn} est : {true_false}")

def saisie_adn(chaine_adn, true_false) : #pppp False
    if true_false == False : #good  
        chaine_adn = list(chaine_adn)#["p","p","p","p"]
        for lettres in range(len(chaine_adn)) : 
            if chaine_adn[lettres] not in {"a","t","c","g"} : 
                chaine_adn[lettres] = random.choice(["a", "t", "c", "g"])
        return "".join(chaine_adn)
    return chaine_adn

new_chaine_adn = saisie_adn(chaine_adn, true_false) 
print(f"Voici la nouvelle chaine de caractere {new_chaine_adn}")


def proportion(chaine_adn, sequance_adn) :
    chaine_adn = list(chaine_adn)
    sequance_adn = list(sequance_adn)
    count = 0

    for lettres_chaine in chaine_adn :
        for lettre_sequance in sequance_adn :
            if lettres_chaine == lettre_sequance :
                count += 1
    return count
compter = proportion(chaine_adn,sequance_adn)
print(f"Il y a {compter} adn identique")