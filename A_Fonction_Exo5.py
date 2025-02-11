chaine_adn = str(input("Donnez une chaîne d'ADN : "))

def verification_adn(chaine_adn) :
    for lettre in chaine_adn :
        if lettre not in "atcg" :
            return False
    return "atcg" in chaine_adn

est_true = verification_adn(chaine_adn)
print(f"Votre séquance {chaine_adn} est {est_true}")