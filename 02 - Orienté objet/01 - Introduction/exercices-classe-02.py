# 2. Créer une classe Feuille 
# Celle-ci devra contenir au minimum 3 attributs différents et 1 méthode

class Feuille:
    def __init__(self, couleur, format, marque):
        self.couleur = couleur
        self.format = format
        self.marque = marque
    
    def vendre(self, nombre):
        print(f"J'ai vendu {nombre} feuilles")

feuille1 = Feuille("blanche", "A4", "Clairefontaine")

feuille1.vendre(25)

