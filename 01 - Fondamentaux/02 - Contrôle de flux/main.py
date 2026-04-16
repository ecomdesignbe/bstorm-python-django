# Contrôle de flux
# 1. Structures conditionnelles
# 2. Structures itératives
# 3. Comprendre les collections

# Structures conditionnelles
## IF-ELSE
## Définitions :
## Structure de contrôle permettant de diriger l'exécution du programme en fonction de la vérification de conditions.
## Les conditions retournent un booléen (True ou False).
## Les blocs de code sont identifiés par l’indentation.
## On utilise elif en Python au lieu de else if.
## Le else est optionnel, il sert de cas par défaut si aucune condition n’est vraie.
## On peut imbriquer des conditions → cela s’appelle le nesting.

score = int(input("Quel est votre score ? "))

if (score >= 90) :
    print("Grade: A")
elif (score >= 80) :
    print("Grade: B")
elif (score >= 70) :
    print("Grade: C")
elif (score >= 60) :
    print("Grade: D")
else :
    print("Grade : F") 

## Quelle est la sortie en console
## Si le score = 71. > Grade C
## Si le score = 780. > Grade A
## Si le score = -154. > Grade F

## La ternaire
## if score >= 50 :
##     result = "reussi"
## else : 
##     result = "raté"

result = "reussi" if score >= 50 else "raté" 
print(result)

## L'opérateur ternaire est un raccourci pour écrire des expressions conditionnelles. Il permet de simplifier des structures de contrôle ifelse ne contenant qu’un if et un else.

###############################################################################################################################

## MATCH
## Définitions :
## Structure de contrôle permettant de choisir parmi plusieurs blocs de code, celui à 
## exécuter en fonction de la valeur d'une expression.
## match compare une expression (ici dayOfWeek) à différents case.
## Chaque case est une valeur possible.
## L’opérateur | permet de regrouper plusieurs valeurs dans un même cas.
## Le caractère _ est un joker (wildcard), équivalent au default.

dayOfWeek = 2

match dayOfWeek :
    case 1 :
        print("Lundi")
    case 2 :
        print("Mardi")
    case 3 | 4 | 5 :            ## L’opérateur | permet de regrouper plusieurs valeurs dans un même cas.
        print("Autre jour")
    case _ :                    ## Le caractère _ est un joker (wildcard), équivalent au default.
        print("Jour invalide")

###############################################################################################################################

# Structures itératives
## BOUCLES WHILE
## Les boucles while sont des structures de contrôle utilisées pour répéter un bloc de code tant qu'une condition est vraie.

## La boucle while
compteur = 0
while compteur < 10 :
    print(compteur)
    compteur += 1

## Test de condition : La condition est vérifiée "avant" chaque itération du bloc de code.
## Exécution : Si la condition est fausse dès le départ, le bloc de code ne sera jamais exécuté.

## Simuler une boucle do while
compteur = 0
while True :
    print(compteur)
    compteur += 1
    if compteur >= 10:
        break

## Test de condition : La condition est vérifiée "après" chaque itération du bloc de code.
## Exécution : Si la condition est fausse dès le départ, le bloc de code sera exécuté 1 fois.

###############################################################################################################################

## BOUCLES FOR
## En Python, la boucle for sert à parcourir une séquence (liste, chaîne de caractères, plage de nombres…).
mot = "Python"
for lettre in mot : 
    print(lettre)

for compteur in range(10): # de 0 à 9
    print(compteur)

###############################################################################################################################

# Comprendreles collections
## Les collections en python :
## En python, comme dans beaucoup d’autres langages de programmation, une collection est une variable qui peut contenir plusieurs
## valeurs à la fois.

## variable stockant une seule valeur
nom_etudiant = "Garb"

## variable stockant plusieurs valeurs
classe_d_etudiant = ["Garb", "Michelle"]

## Les types de collections :
## En Python, il existe 4 grands types de collections : la liste, le tuple, le set et le dictionnaire et 
## elles se différencient par leur comportement vis-à-vis de plusieurs critères.
## Ces critères au nombre de 4 (indexé, ordonné, modifiable, membres duplicables)

### Les caractéristiques des collections - Indexé
### Lorsqu’on dit qu’une collection est indexé, on entend par là que chaque élément qui
### compose la collection peut-être retrouvé grâce à sa position (index) ou à sa clé.

liste_etudiants = [
    "Garb",     # Index = 0
    "Michelle", # Index = 1
    "Etienne"   # Index = 2  
]

### Si je veux récupérer l'etudiant n°2 :
etudiant2 = liste_etudiants[1] # je passe par l'index

etudiant_garb = {
    "nom" : "Garb",     # Clé = nom
    "age" : 22,         # Clé = age
    "ville" : "Paris"   # Clé = ville
}

### Si je veux récupérer l'âge de l'étudiant Garb
age_garb = etudiant_garb["age"] # Je passe par la clé

### Les caractéristiques des collections - Ordonné
### Lorsqu’on dit qu’une collection est ordonnée, cela signifie qu’elle garde les éléments 
### dans le même ordre que celui dans lequel ils ont été ajoutés.

etudiants = ["Alice", "Bob", "Charlie"] 

### Les caractéristiques des collections - Modifiable
### Lorsqu’on dit qu’une collection est modifiable, cela signifie qu’il est possible, après sa création, 
### d’ajouter de nouveaux éléments, d’en supprimer ou d’en modifier.

fruits = ["pomme", "banane", "orange"] 

### Les caractéristiques des collections - Membres dupliqués
### Lorsqu’on dit qu’une collection accepte ou non les membres dupliqués, on s’intéresse à la possibilité d’avoir plusieurs fois 
### la même valeur à l’intérieur de la collection.

fruits = ["pomme", "banane", "pomme"]

### Les caractéristiques des collections - Tableau
### Avant de choisir entre liste, tuple, set ou dictionnaire, il est utile de savoir comment ces structures se comportent. 
### Cette page récapitule les 4 caractéristiques clés qui les distinguent.

### NOM           Indexé          Ordonnée                Modifiable Membre dupliqué
### Liste         OUI             OUI                     OUI        OUI
### Tuple         OUI             OUI                     NON        OUI
### Set           NON             NON                     OUI        NON
### Dictionnaire  OUI (par clé)   OUI (depuis Python 3.7) OUI        NON

### La liste
### Qu’est-ce qu’une liste ?
### Une liste est une collection ordonnée, indexée, modifiable, et qui accepte les doublons.
### En python, on utilise les crochets [] pour la définir.

etudiants = ["Garb", "Michel", "Etienne"] # creer une liste avec des elements

liste_vide_1 = []      # créer une liste vide
liste_vide_2 = list()  # créer une liste vide
elem = etudiants[1]    # Accéder à un élément (par index) "Michel"

### Liste - Modification & Gestion : Avec les listes, on peut ajouter, modifier et supprimer librement.
etudiants = ["Garb", "Michel", "Etienne"]
### Modifie une valeur
etudiants[2] = "Samuel"         # remplace "Michel" par "Samuel"

### Ajouter des éléments
etudiants.append("Thierry")     # ajoute à la fin
etudiants.insert(1, "Méderick") # insère à l'index 1

### Supprimer des éléments
etudiants.remove("Etienne")     # supprime "Etienne"
etudiants.pop(2)                # supprime l'éléments d'index 2
etudiants.clear                 # supprime toute la liste

### Le tuple
### Un tuple est une collection ordonnée, qui peut contenir des doublons, qui est indexée, mais qui, 
### contrairement à liste est non modifiable (immuable).
### Pour déclarer un tuple, on ne passe pas par des [], mais par des ().

etudiants = ("Garb", "Michel", "Etienne")           # avec des ()
etudiant2 = tuple( ("Garb", "Michel", "Etienne") )  # avec le constructeur tuple()

### Tuple- Modification & Gestion : Avec les tuples, impossible de modifier ou de supprimer un élément après la création, 
### par contre, on peut quand même y accéder !

etudiants = ("Garb", "Michel", "Etienne")
etudiants1 = etudiants[1] # Michel

### Le dictionnaire
### Qu’est-ce qu’un dictionnaire?
### Un dictionnaire est une collection ordonnée (depuis Python 3.7) et modifiable qui associe chaque valeur à une clé unique.
### Les clés servent d’index explicite (au lieu de positions numériques).

etudiant = {                                                            # avec des accolades
    "prenom" : "Garb",
    "nom" : "Collector",
    "annee": 2023
}

etudiant_2 = dict(prenom = "Garb", nom = "Collector", annee = 2023 )    # avc la fonction dict()

d1 = {}                                                                 # dictionnaire vide
d2 = dict()

### Dictionnaire - Modification & Gestion
### Le dictionnaire est une collection de paires clé → valeur qui est très utilisé pour représenter des objets ou 
### des données structurées (ex. un étudiant, un produit, un formulaire).

etudiant = {                                                            # avec des accolades
    "prenom" : "Garb",
    "nom" : "Collector",
    "annee": 2023
}

### Accèder aux valeurs
print(etudiant["prenom"])       # "Garb"
print(etudiant.get("nom"))      # "Collector"

### Modifier ou ajouter une entrée 
etudiant["annee"] = 2024        # Modification
etudiant["matricule"] = "JS042" # Ajout

# Supprimer une entrée
etudiant.pop("annee")           # supprime par clé
etudiant.popitem()              # supprime le dernier élément ajouté
etudiant.clear                  # supprime tout

### Le set
### Qu’est-ce qu’un set ?
### Un set est une collection non ordonnée et non indexée. 
### Il est par contre modifiable (on peut ajouter ou supprimer des éléments), mais
### n'accepte pas les doublons (chaque valeur est unique).

noms = {"Garb", "Michel", "Etienne"}        # avec des accolades

noms2 = set(["Garb", "Michel", "Etienne"])  # avec la fonction set()

ensemble_vide = set()

### Set - Modification & Gestion
### Un set = un "sac" de valeurs uniques, sans ordre défini plutôt pratique pour tester l’appartenance (in) et éliminer les doublons !

### Ajouter des éléments
noms.add("Baltazar")            # ajoute un seul élément
noms.update(["Marc", "Petry"])  # ajoute plusieurs éléments

### Supprimer des éléments
noms.remove("Pétry")            # supprime Pétry (erreur si absent)
noms.discard("Phi")             # supprime Phi (ne provoque pas d'erreur si absent)
noms.pop()                      # supprime un élément aléatoire
noms.clear()                    # supprime tout