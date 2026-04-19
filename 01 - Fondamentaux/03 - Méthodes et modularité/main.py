# Méthodes & modularité
# 1. Définition & appel de méthodes
# 2. Paramètres positionnels et nommés, args, kwargs
# 3. Valeurs de retour & portée des variables
# 4. Docstrings & annotations de type
# 5. Modules & import : standard library & modules tiers

## 1. Définition & appel de méthodes
## Qu’est-ce qu’une méthode ?
## En Python, une méthode est un bloc de code réutilisable qui exécute une tâche précise.
## Elle permet d’éviter les répétitions et de rendre le code plus clair et structuré.

# Déclation des méthodes 
def saluer():
    print("Bonjour !")

def prendreCookie():
    return "cookie"

# Appel des méthodes
saluer() # va afficher > Bonjour ! en console.
nourriture = prendreCookie() # initialise la variable avec "cookie"

## Les types de méthodes
## Procédure : Ne retourne rien. Elle exécute une action mais ne fournit pas de résultat à réutiliser.
## Fonction : Retourne une valeur (ici “cookie”). Cette valeur peut ensuite être utilisé dans la suite du programme.

###############################################################################################################################

## 2. Paramètres positionnels et nommés,args, kwargs
## Définition : Moyen de donner des informations à une fonction lors de son appel.
## En Python, on peut passer les paramètres de deux façons :
## Positionnels : l’ordre compte.
## Nommés : on précise le nom du paramètre, peu importe l’ordre.

# Déclarations des méthodes 
def saluer(texte, ponctuation=" ! "):                           # " ! " est une valeur par défaut
    print(f"{texte} {ponctuation}")

def prendreCookie(gout, taille):
    return f"{taille} cookie au {gout}"

# Appel des méthodes
saluer("Hello")                                                 # positionnel : Hello rempli forcément du texte
nourriture = prendreCookie(taille = "grand", gout="chocolat")   # nommé avec un =

## Quand on ne connaît pas d’avance le nombre d’arguments : Python offre deux mécanismes pratiques :
## *args → pour recevoir un nombre variable d’arguments positionnels.
## **kwargs → pour recevoir un nombre variable d’arguments nommés.

# *args
def additionner(*nombres):
    return sum(nombres)

print(additionner(2,3,5))     # 10
print(additionner(1,2,3,4,5)) # 15

# **kwargs
def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(f"{cle} : {valeur}")
afficher_infos(nom = "Alice", age = 25, ville="Paris")

###############################################################################################################################

## 3. Valeurs de retour & portée des variables
## Qu’est-ce qu’une valeur de retour ?
## Jusqu’ici nous avons vu qu’une fonction peut renvoyer un résultat avec le mot-clé return.
## Cette valeur peut ensuite être stockée dans une variable ou réutilisée dans le programme.
## Mais il est également possible de retourner plusieurs valeurs à la fois.

def operations(a, b):
    return a+b, a-b

somme, difference = operations(10, 3)

## Portées des variables (Scope)
## Qu’est-ce que la portée ? La portée définit où une variable est accessible dans le code.
## En Python, on distingue :
## Variable locale → Créée à l’intérieur d’une fonction → accessible uniquement dans cette fonction.
## Variable globale → Définie en dehors d’une fonction → accessible dans tout le script.

def ma_fonction():
    x = 10       # variable locale
    print(x)

ma_fonction()
print(x)         # erreur

y = 20           # variable globale
def autre_fonction():
    print(y)
autre_fonction() # 20 

###############################################################################################################################

## 4. Docstrings & annotations de type
## Définition Docstring : Une docstring (documentation string) est une chaîne de caractères placée 
## au début d’une fonction (ou classe, module, si vous faites de la POO).
## Elle décrit ce que fait la fonction → utile pour l’utilisateur et pour l’autodocumentation.
## Bonne pratique : toujours écrire une docstring claire quand la fonction est destinée à être réutilisée.

def additions(a,b):
    """
        Calcule la somme de deux nombres

        Paramètres:
            a (int ou float) : premier nombre
            b (int ou float) : deuxième nombre

        Retour :
            int ou float : la somme de a et b
    """
    return a + b
print(additions, __doc__) # affiche la docstring

## Annotations de type
## Qu’est-ce que c’est ?
## Les annotations de type permettent d’indiquer les types attendus pour les paramètres et le retour d’une fonction.
## Elles ne bloquent pas l’exécution → Python reste dynamique, mais elles aident à la lisibilité et aux outils de vérification comme l’IDE.
## param: type ( exemple → a: int ) indique le type d’un paramètre.
## -> type ( exemple → -> None ) indique le type du retour, ce qui est utile pour la documentation, la relecture de code et 
## l’autocomplétion dans les IDE

def addition(a: int, b:int) -> int:
    return a + b

def saluer(nom: str) -> None:
    print(f"Bonjour {nom}")

###############################################################################################################################

## 5. Modules & import: standard library &modules tiers
## Qu’est-ce qu’un module ? Un module est un fichier Python qui contient du code réutilisable (fonctions, classes, variables).
## Python fournit une bibliothèque standard de modules très riche (math, random, datetime, os…), 
## mais on peut aussi installer des modules tiers via pip.

# Importer un module (standard library)
import math

print(math.sqrt(16))  # 4.0

# Importer une fonction spécifique : 
from random import randint

print(randint(1, 10)) # nombre aléatoire entre 1 et 10

## Installer un module externe avec pip : Pour installer un module externe, rendez-vous dans un terminal et tapez la commande pip install module.
## pip install requests
import requests
response = requests.get("https://api.github.com")



