"""
Écris un programme qui demande un entier à l’utilisateur.
Si l’utilisateur entre une valeur incorrecte (par ex. du texte), intercepte l’erreur et affiche “Veuillez entrer un nombre valide”.
Si la saisie est correcte, affiche “Merci, vous avez saisi X”.
"""

try:
    nombre = int(input("Entre un entier : "))
except ValueError:
    print("Veuillez entrer un nombre valide")
else:
    print(f"Merci, vous avez saisi {nombre}.")