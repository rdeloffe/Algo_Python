ma_liste = []
print(ma_liste)

##################################################

ma_liste2 = [1,2,3,"Toto",True,["a",True,25]]
print(f"Premier exemple {ma_liste2}")

##################################################

print(f"Second exemple {ma_liste2[0]}")
print(f"Troisieme exemple {ma_liste2[3]}")
print(f"4eme exemple {ma_liste2[-1]}")

##################################################

print(f"Recup le true : {ma_liste2[-1][1]}")
print(f"Recup le true 2 : {ma_liste2[5][1]}")

##################################################

#Modifier un element le premier True
ma_liste2[4] = "titi"
print(f"Titi afficher ? {ma_liste2}")

##################################################

ma_liste3 = [5,3,4,1,2]
print(f"Liste 3 {ma_liste3}")
ma_liste3.sort()
print(f"Liste 3 trier {ma_liste3}")

##################################################

#ajout element a la fin de la liste 
print(f"Liste 2 avant ajout {ma_liste2}")
ma_liste2.append(30)
print(f"Liste 2 apres ajout fin  {ma_liste2}")

#ajout element precis dans la liste 
ma_liste2.insert(2,"tutu")
print(f"Insert index 2 {ma_liste2}")

#Ajouter une liste a une autre 
ma_liste2.extend(ma_liste3)
print(f"Fusion liste 3 dans 2 {ma_liste2}")

##################################################

#Retirer le premier element de la liste
ma_liste2.pop(0)
print(f"Retirer premier element {ma_liste2}")

ma_liste2.remove(2)
print(f"Retirer premier 2 {ma_liste2}")

ma_liste2[4].pop(1)
print(f"Retirer le True dans une liste de liste {ma_liste2}")

##################################################

#Parcours liste 
for element in ma_liste2 :
    print(element)
    
##################################################

ma_variable = True
print(type(ma_variable))






