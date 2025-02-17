import csv
from os import write

#Lecture et affichage de chaque ligne

fichier = open("demo_csv/test.csv" , "rt")
reader = csv.reader(fichier , delimiter=";")
for row in reader :
    print(row)
fichier.close

#Ecriture

fichier2 = open("demo_csv/test.csv" , "wt",newline="")
writer_csv = csv.writer(fichier2,delimiter=";")
writer_csv.writerow(["titi",66,"Gant"])
writer_csv.writerow(["Ottman",85,"Italie"])
writer_csv.writerow(["Rodolf",12,"Chezlabas"])
writer_csv.writerow(["Roco",54,"Habite"])
writer_csv.writerow(["top",61,"nt"])
writer_csv.writerow(["titi",66,"Gant"])
writer_csv.writerow(["titi",66,"Gant"])
fichier2.close()

