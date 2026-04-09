# Type primitifs : entier, flottants, booléens
## INT > Un entier est un nombre sans virgule : positif, négatif ou nul.
age = 12
b = -3
c = 0

## FLOAT > Un flottant est un nombre avec virgule, représenté par un point . en Python.
pi = 3.14
temperature = -5.7

## BOOL > Un booléen représente une valeur vraie ou fausse.
vrai = True
faux = False

age = 18
majeur = age >= 18 # True car 18 >= 18

###############################################################################################################################

# Chaînes de caractères & opérations de base
## STR > Une chaîne est une suite de caractères : lettres, chiffres, symboles, espaces, etc.
prenom = "Alice"
salutation = 'Bonjour'
phrase = "Ceci est une phrase complète."

## CONCATENATION > Concaténation (assemblage de chaînes)
prenom = "Alice"
nom = "Durand"
print(prenom + " " + nom) # Alice Durand

## OPERATION SUR STR   
## Répétition d’une chaîne > On peut répéter une chaîne avec l’opérateur * :
print("Ha" * 3) # HaHaHa

## Longueur d’une chaîne > On peut obtenir le nombre de caractères avec la fonction len().
print(len("Python")) # 6

## Indexation & Slicing > Chaque caractère d’une chaîne a un indice (commençant à 0).
mot = "Python"
print(mot[0])  # P
print(mot[1])  # y
print(mot[-1]) # n (dernier caractère)
print(mot[0:3])  # Pyt (caractère d'indice 0 à 2)
print(mot[2:])   # thon (du 3e caractère jusqu'à la fin)

## Interpolation > L’interpolation de chaînes consiste à insérer directement des variables dans une chaîne de caractères.
prenom = "Alice"
age = 25
print(f"Je m'appelle {prenom} et j'ai {age} ans.") # Je m'appelle Alice et j'ai 25 ans.

###############################################################################################################################

# Opérateurs : arithmétiques, decomparaison,... Liste non exhaustive (Opérateurs de Bit, d’Instance, Ternaire,...)
## Les opérateurs d’affectation :
## =  : Affectation usuel            > x = 5
## += : Affectation + addition       > x += 3 <> x = x + 3
## -= : Affectation + soustraction   > x -= 3 <> x = x - 3
## *= : Affectation + multiplication > x *= 3 <> x = x * 3
## /= : Affectation + division       > x /= 3 <> x = x / 3

## Les opérateurs relationnels :
## <  : Inférieur à         > r = ( 5 < 7 )  <> true
## >  : Supérieur à         > r = ( 5 > 5 )  <> false
## <= : Inférieur ou égal à > r = ( 5 <= 5 ) <> true 
## >= : Supérieur ou égal à > r = ( 5 >= 2 ) <> true 
## == : Egal à              > r = ( 5 == 5 ) <> true
## != : Différent de        > r = ( 5 != 5 ) <> false 

## Les opérateurs logiques :
## AND : AND logique > r = ( true && false ) <> false
## OR  : OR logique  > r = ( true || false ) <> true
## !   : Négation    > r = !( true )           <> false

## Les opérateurs arithmétique
## + : Addition et concaténation > x = 2 + 3 <> 5
## - : Soustration               > x = 4 - 3 <> 1
## * : Multiplication            > x = 2 * 3 <> 6
## / : Division                  > x = 6 / 3 <> 2
## % : Modulo                    > x = 7 % 3 <> 1 ( Reste ) 
 
## Opérationd’écriture :
## Print() : Pour interagir avec l’utilisateur, il est possible de lire la saisie de la console.
## Pour cela, il faut utiliser la méthode « input("message") », qui va permettre de récupérer la valeur entrée par l'utilisateur en format texte.
age = input("Entrez votre age : ") 
# age est actuellement de type str, il faut le convertir
age_en_int = int(age) 
# Attention, la valeur récupérée sera toujours de type texte, une conversion est nécessaire pour la transformer en entier, réel,...

###############################################################################################################################

# Conversion de types
## Fonctions utilitaires
## Il existe des méthodes permettant de convertir une variable vers un type donné
## int(...) : Conversion vers un entier de type "int"
## float(...) : Conversion vers un nombre à virgule
## str(...) : Transformation vers du texte
a = 10
b = float(a)  # 10.0
print(b, type(b))
c = int(3.99) # 3 (tronqué)
print(c, type(c))




