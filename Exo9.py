#Critère candidature
age = int(input("Quelle est votre age ? "))
salaire = float(input("Combien voulais vous par an € ? "))
xp = int(input("Combien d'année d'xp avez vous ? "))

if age > 30 and salaire <= 40000 and xp > 5 :
    print("Vous etre pris")

elif age < 30 and salaire <= 40000 and xp > 5 :
    print ("Trop jeune")

elif age > 30 and salaire >= 40000 and xp > 5 :
    print("Salaire trop élever")

elif age > 30 and salaire <= 40000 and xp < 5 :
    print("Pas assez d'xp")
else :
    print("Vous n'etes pas pris")