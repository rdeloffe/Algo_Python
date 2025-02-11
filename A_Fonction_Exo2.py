a = int(input("Choisir un premier nombre :"))
b = int(input("Choisir un second nombre :"))

def soustraire(a, b) :
    return a - b 
    
resultat = soustraire(a,b)
print(f"Je soustrais {a} a {b} qui donne {resultat}")