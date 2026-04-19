# Demande à l’utilisateur de saisir une série de nombres séparés par des espaces.
# Convertis chaque valeur en entier et calcule leur somme.
# Si l’utilisateur entre une valeur non numérique, intercepte l’erreur et affiche “Veuillez entrer uniquement des nombres”.

try:
    print("Somme =", sum(int(x) for x in input("Entrer des nombres séparés par des espaces : ").split()))
except ValueError:
    print("Veuillez entrer uniquement des nombres")




