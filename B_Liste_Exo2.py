liste_notes = []
for i in range (1,5) :
    demande_note = int(input(f"Donne la note {i} sur /20 : "))
    if demande_note <= 20 :
        liste_notes.append(f"Note {i}: {demande_note} / 20")
    else : 
        print("Note trop haute")
        demande_note = int(input("Donne moi une nouvelle note /20 : "))
print(liste_notes)

    
    