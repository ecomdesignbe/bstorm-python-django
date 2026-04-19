# Créer, puis manipuler un fichier au format JSON à l’aide la méthode open()
# Ps: Importer la librairie JSON.
# Passer par la méthode dump() pour écrire dans le fichier
# Passer par la méthode load() pour lire le contenu du fichier

import json

data = {
    "nom": "Steve",
    "age": 46,
    "ville": "Bruxelles"
}

with open(r"01 - Fondamentaux\05 - IO & manipulation de fichiers\data.json", "w") as f:
    json.dump(data, f)

with open(r"01 - Fondamentaux\05 - IO & manipulation de fichiers\data.json", "r") as f:
    content = json.load(f)

print(content)

