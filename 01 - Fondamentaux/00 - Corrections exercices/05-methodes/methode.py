"""
En python, comme dans pas mal les langages, on retrouve ce qu'on appelle les méthodes.

Celles-ci se décomposent en 2 familles :
"""

"""
1. Les fonctions :
Une fonction est une méthode qui renvoie une valeur.
En gros qu'on utilise lors d'opération.

On retrouve PRESQUE toujours un return dans une fonction.

Ce return signifie, tu peux lors de l'appelle de la fonction, stocker un résultat dans une variable
"""
def addition(a, b):
    return a + b

result = addition(3, 4)

"""
2. Les procédures
Une procédure est une méthode qui ne retourne rien on l'utilise pour par exemple afficher du texte
"""

def print_bonjour():
    print("Bonjour")

# result = print_bonjour() ❌ Erreur => Je n'ai pas de return dans la méthode donc je ne peux récupérer de résultat.