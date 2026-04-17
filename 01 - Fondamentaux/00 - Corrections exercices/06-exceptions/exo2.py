"""
Demande à l’utilisateur de saisir une série de nombres séparés par des espaces.
Convertis chaque valeur en entier et calcule leur somme.
Si l’utilisateur entre une valeur non numérique, intercepte l’erreur et
affiche “Veuillez entrer uniquement des nombres”.
"""
from enum import nonmember

try:
    saisie = input("Entre des nombres avec des espaces : ")
    nombres = [int(x) for x in saisie.split()]
    print("Somme = ", sum(nombres))
except ValueError:
    print("Que des nombres !")