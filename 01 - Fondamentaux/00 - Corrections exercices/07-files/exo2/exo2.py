"""
Faites de même avec un fichier de type csv.
Ps: Importer la libraire CSV.

Passer par la création d’un reader et une boucle FOR pour lire le contenu d’un fichier
Passer par la création d’un writer et la méthode writerow() pour écrire une ligne dans un fichier
"""

import csv

with open("personne.csv", "w", newline="") as fichier:
    writer = csv.writer(fichier)
    writer.writerow(["nom", "age", "ville"])
    writer.writerow(["ibrahim", "26", "Paris"])
    writer.writerow(["Hatim", "28", "Monaco"])

with open("personne.csv", "r") as fichier:
    reader = csv.reader(fichier)

    for ligne in reader:
        print(ligne)
