# Écris un programme qui demande un entier à l’utilisateur.
# Si l’utilisateur entre une valeur incorrecte (par ex. du texte), intercepte l’erreur et affiche “Veuillez entrer un nombre valide”.
# Si la saisie est correcte, affiche “Merci, vous avez saisi X”.

try:
    demande_entier = int(input("Entre un entier :"))
    print("merci, vous avez saisi", demande_entier)
except:
    print("Veuillez entrer un nombre valide")


