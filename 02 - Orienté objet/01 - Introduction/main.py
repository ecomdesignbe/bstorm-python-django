# Introduction à l’Orienté Objet :
# 1. Qu’est-ce qu’un paradigme ?
# 2. Le principe de classe
# 3. L’instanciation
# 4. Attributs & Méthodes
# 5. Méthode spéciale : le constructeur

## 1. Qu’est-ce qu’un paradigme?
## « Un paradigme, c'est comme une 'façon de penser' pour organiser et écrire du code. »
## Il rassemble des concepts et des pratiques permettant de lutter contre des problèmes récurents en programmation.

## Imaginez qu'on vous donne des briques pour construire un bâtiment : un paradigme vous dit comment les assembler
## pour que tout soit solide et efficace.

## « L'orienté objet, c'est une façon de penser le développement de logiciels comme une collection d'objets. »

## Imagine que dans la vraie vie, tout ce que tu vois autour de toi, que ce soit un téléphone, une voiture ou
## même une chaise, puisse être vu comme un "objet" lui même définit par ses caractéristiques et ses usages.
## C'est exactement ce que l'on fait en programmation orienté objet.

## « En orienté objet, un objet se caractérise par des données le décrivant (attributs ou propriétés) et
## par les actions qu’il peut accomplir (méthodes ou comportement). »

## Maintenant que nous savons ce qu’est l’orienté objet, voyons pourquoi tant de développeurs l’utilisent !
## Simplicité et Organisation : La POO, c'est comme avoir des boîtes bien étiquetées pour ranger ton code ! 
##                              Plus facile à retrouver, plus facile à comprendre.

## Réutilisation du Code      : Imagine que tu construises des Lego : une fois que tu as créé une pièce, 
##                              tu peux la réutiliser autant de fois que tu veux dans différents projets !

## Popularité et Support      : Java, Python, C++, C#, TypeScript... Tous ces langages parlent la même langue : l'orienté objet.
##                              Une fois que tu le maîtrises, tu peux facilement passer de l'un à l'autre !

###############################################################################################################################

## 2. Le principe de classe
## En orienté objet, une classe est un plan utilisé pour créer des objets ayant les mêmes attributs et comportements.
## Imagine une usine produisant en quantité un produit. Par exemple un modèle de téléphone.
## Une fois le modèle conceptualisé, l’usine peut en fabriquer à la chaîne.
## En orienté objet, une classe fonctionne comme ce modèle.

class GarbDroid: # Définition de la classe
    def __init__(self, marque, modele, etat="neuf"):
        self.marque = marque   # Attribut
        self.modele = modele   # Attribut
        self.etat = etat       # Attribut
    
    def appeler(self, numero): # Methode
        print(f"Appel du numéro : {numero} en cours...")

## Lorsqu’on développe en Python, il n’est pas question de faire n’importe quoi, quelques bonnes pratiques sont à prendre en compte !
## Évitez la redondance : Par exemple, si vous avez un attribut date_naissance, il n'est pas nécessaire d'ajouter un attribut age, 
##                        car celui-ci peut être calculé directement à partir de la date de naissance.
## Une classe par fichier : En Python, chaque fichier peut contenir plusieurs classes mais doit n’en contenir qu’une.

