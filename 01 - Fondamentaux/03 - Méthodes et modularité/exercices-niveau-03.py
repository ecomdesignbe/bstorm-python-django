# Écris une fonction carre_et_cube qui prend un nombre et retourne deux valeurs : son carré et son cube.
# Stocke le résultat dans deux variables.
# Affiche-les.
#Teste l’utilisation d’une variable locale (à l’intérieur de la fonction) pour montrer qu’elle n’est pas accessible depuis l’extérieur.
def carre_et_cube(nombre):
    carre = nombre ** 2
    cube = nombre ** 3
    variable_locale = "Je suis une variable locale"
    return carre, cube

# Stockage des résultats dans deux variables
resultat_carre, resultat_cube = carre_et_cube(5)

# Affichage
print("Carré :", resultat_carre)
print("Cube :", resultat_cube)

# Test de la variable locale
print(variable_locale)  # Provoque une erreur
