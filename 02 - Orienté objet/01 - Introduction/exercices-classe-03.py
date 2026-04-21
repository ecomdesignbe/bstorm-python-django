# 3. Créer une classe Compte Bancaire :
# Celle-ci devra contenir au minimum 3 attributs différents et 1 méthode.

class CompteBancaire:
    def __init__(self, nom, prenom, numero_compte):
        self.nom = nom
        self.prenom = prenom
        self.numero_compte = numero_compte
    
    def retrait(self, somme_argent):
        print(f"Vous avez retiré {somme_argent} €")

compte1 = CompteBancaire("Steve", "Vandenbossche", "BE123456789")
compte1.retrait(543)
