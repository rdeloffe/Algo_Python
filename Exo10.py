

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

while reponse > 3 or reponse < 1:
    print("Non")
    reponse = float(input("Choisi un new entre 1 et 3 :"))
else :
    print ("Cest OK")






    


