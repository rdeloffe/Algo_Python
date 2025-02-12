le_mot_if = str(input("Choisie un mot : "))
def compter_a_if () :
    count = 0
    for lettre in le_mot_if :
        if lettre != "a" :
            count += 1
    return count

coumpter = compter_a_if()
print(f"Dans le mot {le_mot_if} il y a {coumpter} A ")  


#########################################

le_mot = str(input("Choisie un mot : "))

def compter_a () :
    return(le_mot.count('a'))  

count = compter_a()
print(f"Il y a {count} a")