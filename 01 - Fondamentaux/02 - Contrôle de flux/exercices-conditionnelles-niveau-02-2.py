# Reprendre l’exercice 2.1 mais utiliser match-case (Python ≥ 3.10) avec des gardes (case n if condition:)
# pour stocker directement la catégorie dans une variable, puis l’afficher.
# Observer la lisibilité par rapport au if / elif / else.

note = int(input("Entrez votre note ? "))

match note :
    case n if n == 100 :
        categorie = "Extraordinaire"
    case n if n >= 90 :
        categorie = "Excellent"
    case n if n >= 80 :
        categorie = "Genial"
    case n if n >= 70 :
        categorie = "Top"
    case n if n >= 60 :
        categorie = "Bravo"
    case n if n >= 50 :
        categorie = "Tout juste"
    case n if n >= 40 :
        categorie = "On repassera"
    case n if n >= 30 :
        categorie = "What the f***"
    case n if n >= 20 :
        categorie = "Pénible"
    case n if n >= 10 :
        categorie = "A l'année prochaine"
    case _ :
        categorie = "Ridicule"

print(categorie)