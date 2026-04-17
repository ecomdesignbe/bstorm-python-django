"""
Crée un dictionnaire représentant un étudiant avec les clés : "nom"
,
"age"
,
"ville".
Affiche la valeur associée à la clé "nom".
Modifie l’âge de l’étudiant.
Ajoute une nouvelle clé "note" avec une valeur.

"""

etudiant = {
    "nom": "Mauritcio",
    "age": 25,
    "ville": "aze"
}

print(etudiant["nom"])
etudiant["age"]= 21
etudiant["note"]= 18

print(etudiant)