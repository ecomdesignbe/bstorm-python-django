# Crée un dictionnaire représentant un étudiant avec les clés : "nom" , "age" , "ville".
# Affiche la valeur associée à la clé "nom".
# Modifie l’âge de l’étudiant.
# Ajoute une nouvelle clé "note" avec une valeur.

etudiant = {
    "nom" : "Steve",
    "age" : 46,
    "ville" : "bruxelles"
}

print(etudiant["nom"])

etudiant["age"] = 50

print(etudiant["age"])

etudiant["note"] = 20

print(etudiant)