"""
Crée un tuple représentant les coordonnées d’un point en 2D (x, y).
Affiche chaque coordonnée séparément.
Explique pourquoi tu ne peux pas modifier la valeur de x.
"""

point = (4, 7)

print(f"""
x = {point[0]}
y = {point[1]}
""")

print("""Un tuple est immuable: on ne peut pas modifier ses éléments après création.""")