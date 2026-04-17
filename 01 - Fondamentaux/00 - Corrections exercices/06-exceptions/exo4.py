"""
Demande à l’utilisateur de saisir 5 entiers dans une boucle for.
Utilise try / except pour gérer les erreurs de saisie.
Si une valeur incorrecte est saisie, affiche un message et redemande l’entrée pour que le programme obtienne bien 5 entiers valides au total.
À la fin, affiche la liste des entiers saisis.
"""

entiers = []

while len(entiers) < 5:
    try:
        valeur = int(input(f"Entre l'entier suivant :"))
        entiers.append(valeur)
    except ValueError:
        print("Erreur de saisie, again")

print("Liste : ", entiers)
