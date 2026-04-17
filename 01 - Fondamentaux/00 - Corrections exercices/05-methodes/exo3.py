"""
Écris une fonction carre_et_cube qui prend un nombre et
retourne deux valeurs : son carré et son cube.
Stocke le résultat dans deux variables.
Affiche-les.

Teste l’utilisation d’une variable locale (à l’intérieur de la fonction)
pour montrer qu’elle n’est pas accessible depuis l’extérieur.
"""

def carre_et_cube(nombre):
    variable_locale = "je suis locale"
    return nombre**2, nombre**3

carre, cube = carre_et_cube(3)

print("Carré : ", carre)
print("Cube : ", cube)

# print(variable_locale) -> Erreur la variable n'est disponible que dans la méthdoe
print("Une variable locale n'est accessible qu'à l'intérieur de la méthode dans laquelle elle est déclarée")

