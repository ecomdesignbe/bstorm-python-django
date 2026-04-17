"""
Demander à l'utilisateur de saisir un entier, détecter sa parité et afficher le résultat en console.
"""

nombre = int(input("Entre un entier :"))

if nombre % 2 == 0:
    print("Le nombre est pair !")
else :
    print("Le nombre est impair !")