max = 0
for i in range (1,7) :
    depart = int(input(f"Chiffre {i}: "))
    if depart > max :
        max = depart
print (f"De vos nombre c'est le nombre {max} le plus grand")