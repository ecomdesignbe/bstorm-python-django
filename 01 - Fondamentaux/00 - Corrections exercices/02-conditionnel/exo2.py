# region EXO 2.1
"""
Demander à l'utilisateur de saisir une note entre 0 et 100 et
utiliser la structure if-else pour classifier la note en différentes catégories.
( Exemple : entre 0 & 10 : ridicule )
"""
note = int(input("Entre une note entre 0 et 100 :"))

if 0 <= note <= 10:
    categorie = "ridicule"
elif note < 30:
    categorie = "faible"
elif note < 50:
    categorie = "insuffisant"
else:
    categorie = "Réussi ! "

print(categorie)
# endregion


# region EXO 2.2
"""
Reprendre l’exercice 2.1 mais utiliser match-case (Python ≥ 3.10) avec des gardes (case n if condition:)
pour stocker directement la catégorie dans une variable, puis l’afficher.
Observer la lisibilité par rapport au if / elif / else.
"""
note = int(input("Entre une note entre 0 et 100 :"))

match note:
    case n if 0 <= note <= 10:
        categorie = "ridicule"
    case n if note < 30:
        categorie = "faible"
    case n if note < 50:
        categorie = "insuffisant"
    case _:
        categorie = "Réussi ! "

print(categorie)
# endregion