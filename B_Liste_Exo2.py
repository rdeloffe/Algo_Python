liste_notes = []
for i in range (1,16) :
    demande_note = int(input(f"Donne la note {i} sur /20 : "))
    while demande_note > 20 :
        print("Note trop haute")
        demande_note = int(input(f"Redonne moi la note {i} /20 : "))
    liste_notes.append(f"Note {i}: {demande_note}/20")
print(liste_notes)

    
    