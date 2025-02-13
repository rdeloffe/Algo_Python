mon_tuple = (1,2,3,4)
print(f"mon jolie tuple {mon_tuple}")

#Acceder a un element 
print(f"Premier element {mon_tuple[0]}")
print(f"Dernier element {mon_tuple[-1]}")

#unpacking
a,b,c,_ = mon_tuple
print (f"Déballage a = {a} b = {b} c = {c} ")

def recupere_nombre(nombre) :
    return nombre, nombre * 2
print(recupere_nombre(3))

valeur_1 , valeur_2 = recupere_nombre(2)
print(f"Valeur 1 : {valeur_1} Valeur 2 : {valeur_2}")