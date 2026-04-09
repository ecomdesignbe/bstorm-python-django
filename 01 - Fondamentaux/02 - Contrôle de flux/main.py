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