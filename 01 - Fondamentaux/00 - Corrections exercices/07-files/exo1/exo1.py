"""
Créer, puis manipuler un fichier au format JSON à l’aide la méthode open()
Ps: Importer la librairie JSON.

Passer par la méthode dump() pour écrire dans le fichier
Passer par la méthode load() pour lire le contenu du fichier
"""
import json

donnees = {
    "nom": "Noah",
    "age": 35,
    "ville": "Paris"
}

with open("etudiant.json", "w") as fichier:
    json.dump(donnees, fichier)

with open("etudiant.json", "r") as fichier:
    contenu = json.load(fichier)

print(contenu)