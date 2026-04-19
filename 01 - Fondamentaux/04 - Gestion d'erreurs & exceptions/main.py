# Gestion des erreurs et exceptions
# 1. Le mécanisme des exceptions 
# 2. try / except / else / finally

## 1. Le mécanisme des exceptions 
## Qu’est-ce que c’est ?
## Les exceptions sont des erreurs prévues et contrôlées : on peut les attraper et y réagir plutôt que de laisser le programme planter.

print("Début du programme")
# Ici Python lève une exception ZeroDivisionError et le programme s'arrête
x = 10 / 0 # Erreur : Division par zéro
print("Fin du programme")

## Pourquoi gérer les exceptions ?
## Éviter les plantages brutaux.
## Fournir un message clair à l’utilisateur.
## Continuer l’exécution du programme malgré l’erreur.

###############################################################################################################################

## 2.try / except / else / finally
## Comment gérer les exceptions :
## On peut gérer les exceptions grâce aux différents outils : try / except / else / finally

## Le bloc try / except : il permet de tester un bloc de code et d’intercepter les exceptions.
try:
    x = 10 / 0
except ZeroDivisionError: # Sans except, le programme plante. Avec except, il continue normalement.
    print("Erreur : division par zéro interdite")

## Ajouter else : Le bloc else s’exécute uniquement si aucune exception n’a été levée.
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Erreur : division par zéro")
else:
    print("Succès, le résultat est", x)

## Ajouter finally : Le bloc finally s’exécute toujours, qu’il y ait une erreur ou non (utile pour libérer des ressources).
try:
    fichier = open("test.txt", "r")
    contenu = fichier.read()
except FileNotFoundError:
    print("Fichier introuvable")
finally:
    print("Fin de l'opération")
