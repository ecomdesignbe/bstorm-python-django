# Demande à l’utilisateur de saisir 5 entiers dans une boucle for.
# Utilise try / except pour gérer les erreurs de saisie.
# Si une valeur incorrecte est saisie, affiche un message et redemande l’entrée pour que le programme obtienne bien 5 entiers valides au total.
# À la fin, affiche la liste des entiers saisis.

entiers = []

for i in range(5):
    while True:
        try:
            valeur = int(input("Entrez un entier : "))
            entiers.append(valeur)
            break
        except ValueError:
            print("Ce n'est pas un entier, veuillez réessayer.")

print("Liste des entiers saisis :", entiers)