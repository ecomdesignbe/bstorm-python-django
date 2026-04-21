# 1. Créer une classe Stylo :
# Celle-ci devra contenir au minimum 3 attributs différents et 1 méthode

class Stylo:
    def __init__(self, marque, couleur, etat):
        self.marque = marque
        self.couleur = couleur
        self.etat = etat
    
    def ecrire(self, type_stylo):
        print(f"J'écris avec un stylo {type_stylo}")

stylo1 = Stylo("Bic", "Bleu", "Neuf")

stylo1.ecrire("à bille")



