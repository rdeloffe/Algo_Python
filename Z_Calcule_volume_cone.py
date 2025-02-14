#A partir dela saisie d'un rayon et d'une hauteur, calcule le volume d'un cone droit
import math
rayon = float(input("Donne moi le rayon (en cm) :"))
hauteur = float(input("Donne moi la hauteur (en cm) :"))


volume = ( (rayon * rayon) * math.pi  * hauteur) / 3

print("Le volume de ce cone est de ", volume,"cm²")