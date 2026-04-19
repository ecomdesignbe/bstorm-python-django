# Entrée/Sortie & manipulation de fichiers
# 1. Lecture et écriture de fichiers texte
# 2. Gestion de contexte avec with
# 3. Chemins de fichiers : module os vs pathlib

## 1. Lecture et écriture de fichiers texte
## Fichier : Lecture
## La lecture d’un fichier en python se fait assez simplement, on passe tout d’abord par le mot réservé with et la méthode open().
## Celle-ci prend plusieurs paramètres :
## Le nom du fichier
## Le mode (par exemple lecture ou écriture)
## Le type d’encodage du fichier.
with open("fichier.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

## Fichier : Ecrire
## Il est également possible d’écrire un fichier en passant par la même fonction via le mode write.
with open("fichier.txt", "w", encoding="utf-8") as f:
    f.write("Bonojour à tous !")

## Fichier : Modifier
## Nous pouvons aussi via add, ajouter une ligne à un fichier existant.
with open("fichier.txt", "a", encoding="utf-8") as f:
    f.write("Nouvelle ligne !")

## Fichiers : De manière générale, quand on veut manipuler des fichiers en python on passe par la méthode open.
# Nous avons pris pour exemple un fichier texte, mais nous aurions pu choisir sans souci d’autre type d’extension.
# Ps: Selon l’extension, il peut y avoir quelques nuances.

###############################################################################################################################

