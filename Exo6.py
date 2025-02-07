#Cout des copie
prix = int
copie = int(input("Combien de copie vous voulez faire ? "))

if copie <= 10 :
    prix = copie * 0.5
    print("Cela vous coute", prix,"€")

elif (copie > 10 and copie <= 20) :
    prix = copie * 0.4
    print("Cela vous couteras", prix,"€")

else :
    prix = copie * 0.3
    print("Cela vous couteras",prix,"€")
