a = float(input("Choisir un premier nombre :"))
b = float(input("Choisir un second nombre :"))

def soustraire(a, b) :
    return a - b #Renvoie le resultat de a - b
    
resultat = soustraire(a,b)
print(f"Le resultat de {a} - {b} = {resultat}")