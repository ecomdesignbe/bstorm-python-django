# Crée un tuple représentant les coordonnées d’un point en 2D (x, y).
# Affiche chaque coordonnée séparément.
# Explique pourquoi tu ne peux pas modifier la valeur de x.
x = 2
y = 4
coordonnees = (x, y)

print(coordonnees[0])
print(coordonnees[1])

# Les tuples sont immuables en Python. Cela signifie qu’une fois créés, leurs éléments ne peuvent pas être changés.
# Par exemple, ceci provoquera une erreur :
# coordonnees[0] = 10
# Erreur : TypeError: 'tuple' object does not support item assignment