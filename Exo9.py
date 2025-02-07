#Critère candidature
age = int(input("Quelle est votre age ? "))
salaire = float(input("Combien voulais vous par an € ? "))
xp = int(input("Combien d'année d'xp avez vous ? "))

if age > 30 and salaire <= 40000 and xp > 5 :
    print("Vous etre pris")
else :
    print("Vous n'etes pas pris")