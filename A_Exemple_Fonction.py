def hello_world() : 
    # print("Hello World !!!")
    return ("Hello World !!!")
ma_variable = hello_world()
print(f"Valeur de ma_variable {ma_variable}")


################################################


def dire_bonjour(nom,prenom):
    print(f"Bonjour {nom} {prenom}")

dire_bonjour('toto','tata')
dire_bonjour('tutu' , 'tata')


################################################


def say_hello(name = "Loic") :
    print(f"Bonjour {name}")

say_hello("Antoine")


################################################


def nombre() :
    a = 2
    b = 5
    c = 9
    return a, b, c
lettre_a, lettre_b, lettre_c = nombre()
print(lettre_c)


################################################
def retourne_oui_si_pair(nombre) :
    if nombre % 2 == 0:
        print("Oui")
    else :
        print("Non")

nb = int(input("Donner un nombre : "))
retourne_oui_si_pair(nb)

# # OU 

def retourne_oui_si_paire(nombre) :
    if nombre % 2 == 0 :
        return "oui"
    else :
        return "non"

resultat = retourne_oui_si_paire(nb)
print(f"Votre chiffre {nb} est-il paire ? : {resultat}")


################################################
