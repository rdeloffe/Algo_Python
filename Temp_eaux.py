#Temperature
temp = float(input("Quelle est la temperature de l'eau ? "))

if temp <= 0 :
    print ("L'eau est SOLIDE")
elif 0 < temp <= 100 :
    print("L'eau est Liquide")
else :
    print("L'eau est GAZEUX")