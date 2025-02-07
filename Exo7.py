#Etat enfant 
age = int(input("Quel âge a votre enfant ? "))

if 0 <= age <= 6:
    print("Baby")
elif 7 <= age <= 8:
    print("Poussin")
elif 9 <= age <= 10:
    print("Pupille")
elif 11 <= age <= 12:  
    print("Minime")
elif age >= 13:
    print("Cadet")
else:
    print("Âge invalide")  
