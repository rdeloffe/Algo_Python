

# for nb in range (5) :
#     reponse = int(input("Choisi un nombre entre 1 et 3 :"))
#     while reponse not in [1 , 2 , 3] :
#         print("Non OK")
#         nb = nb + 1
#         reponse = int(input("Choisi un nouveau nombre entre 1 et 3 :"))
#         print(nb)
#     break

# print("C'est ok")


reponse = float(input("Choisi un nombre entre 1 et 3 :"))
chance = 1

while reponse > 3 or reponse < 1 or chance < 5:
    print("Non")
    chance = chance + 1
    print(chance)
    reponse = float(input("Choisi un new entre 1 et 3 :"))
    if chance > 4 :
        print("Vous n'avez plus de chance")
        break
else :
    print ("Cest OK")






    


