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

## 2. Gestion de contexte avec with
## Pourquoi utiliser with ?
## En Python, quand tu travailles avec certaines ressources (comme un fichier, une connexion réseau, ou une base de données), 
## tu dois les ouvrir pour les utiliser… puis les fermer correctement après usage.
##
## Pourquoi faut-il fermer une ressource ?
## Si tu oublies de fermer une ressource, plusieurs problèmes peuvent apparaître :
## Fuite de mémoire : la ressource continue d’occuper de la place inutilement
## Blocage du fichier : impossible de le modifier ou de le rouvrir ailleurs
## Limite du système atteinte : trop de fichiers ouverts en même temps → erreurs
## Comportement imprévisible : données non sauvegardées correctement
##
## Le rôle de with : Le mot-clé with permet de gérer automatiquement ces ressources.
## Il agit comme un gardien :
## Il ouvre la ressource au début
## Il s’assure qu’elle est toujours fermée à la fin, même en cas d’erreur

## exemple sans with
f = open("mon_fichier.txt", "r")
contenu = f.read()
f.close()

## exemple avec with
with open("mon_fichier.txt", "r") as f:
    contenu = f.read()

###############################################################################################################################

## 3. Chemins de fichiers : module os vs pathlib
## Pourquoi gérer les chemins de fichiers ? 
## Il n’est pas rare en Python de devoir manipuler des fichiers.

## Pour y accéder correctement, tu dois :
## Construire des chemins valides
## Gérer les différences entre systèmes (Windows, Linux, Mac)
## Éviter les erreurs de concaténation

## Problèmes avec une mauvaise gestion des chemins
## Si les chemins sont mal construits :
## Erreurs de fichier introuvable : mauvais séparateurs (/ vs \)
## Code non portable : fonctionne sur un OS mais pas sur un autre
## Concaténation fragile : erreurs avec les chaînes de caractères
## Maintenance difficile : chemins peu lisibles

## Le module os
## Pendant votre carrière vous risquez de tomber sur des projets avec du vécu qui utilisent peut-être os.
import os
chemin = os.path.joint("dossier", "fichier.txt")

## Le module pathlib
## Pathlib est l’approche moderne (depuis python 3.4) et recommandée pour la gestion des chemins en python.
## Il agit comme un gestionnaire intelligent :
## Il construit automatiquement les bons chemins
## Il s’adapte au système d’exploitation
## Il simplifie les opérations sur les fichier
from pathlib import Path
chemin = Path("dossier") / "fichier.txt"

if chemin.exists():
    print("Existe")

## Comparaison - Cas concret
## Tu veux chercher tous les fichiers .txt dans un dossier et ses sous-dossiers.

import os
for root, dirs, files in os.walk("projet"):
    for file in files:
        if file.endswith(".txt")
            print(os.path.join(root,file))

from pathlib import Path
for fichier in Path("projet").rglob("*.txt"):
    print(fichier)
