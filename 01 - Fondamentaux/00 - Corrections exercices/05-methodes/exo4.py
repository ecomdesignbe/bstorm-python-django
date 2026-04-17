"""
Écris une fonction aire_cercle(rayon: float) -> float qui calcule l’aire d’un cercle.
Ajoute une docstring expliquant les paramètres et la valeur de retour.
Utilise le module math pour obtenir la valeur de π.

"""

import math
def aire_cercle(rayon: float) -> float:
    """
    Calcule l'aire d'un cercle à partir de son rayon

    :param rayon: rayon du cercle
    :return:  aire du cercle
    """
    return math.pi * rayon ** 2

print(aire_cercle(2.5))