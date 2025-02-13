liste_notes = []

Instruction = int(input(
    "Choisir la methode de la saisie des notes :\n"
    "1. Nombre exact \n"
    "2. Saisie a l'infini (inscrire une note néga pour stopper)\n"
    "Votre choix : "
))

if Instruction == 1 :
    nb_notes = int(input("Combien de notes voulez vous inscrire ? "))
    for nb_notes in range (1,nb_notes+1) :
        demande_note = float(input(f"Note {nb_notes} sur /20 :"))
        while demande_note > 20 :
            print("Note trop haute")
            demande_note = int(input(f"Redonne moi la note {nb_notes} /20 : "))
        liste_notes.append(demande_note)
    print(f"{liste_notes}\n")


if Instruction == 2 :
    demande_note = 1
    while demande_note > 0 :
        demande_note= float(input("Donne moi un note /20 (note néga = stop) : "))

        while demande_note > 20 :
            print("Note trop haute")
            demande_note = int(input(f"Redonne moi la note  /20 : "))
        liste_notes.append(demande_note)
    liste_notes.pop(-1)
    print(f"{liste_notes}\n")



    Menu = int(input("Choisissez ce que vous voulez faire avec ces notes :\n"
        "1. Voir la note maximal\n"
        "2. Voir la note minimal \n"
        "3. Voir la moyenne \n"
        "Votre choix : "  
    ))

    if Menu == 1 :
        max_notes=liste_notes[0]
        for nb in liste_notes :
            if nb > max_notes :
                max_notes = nb
        print(f"La note maximale est {max_notes}")

    if Menu == 2 :
        min_notes=liste_notes[0]
        for nb in liste_notes :
            if nb < min_notes :
                min_notes = nb
        print(f"La note la plus basse est {min_notes}")

    if Menu == 3:  
        somme_notes = sum(liste_notes)  
        nombre_notes = len(liste_notes)  
        if nombre_notes > 0:  
            moyenne = somme_notes / nombre_notes  
            print(f"La moyenne des notes est {moyenne:.2f}")  


    



    




