"""
Écrire un programme qui calcule et affiche les n premiers termes de la suite de Fibonacci,
où n est un nombre entier donné par l'utilisateur.

Faire en sorte que le programme choisisse l’un de ces termes au hasard et
qu’il en calcule la factorielle, offrir à l’utilisateur la possibilité d’essayer
de retrouver le terme de la suite qui a été choisi pour la factorielle.
"""

import random
import math

n = int(input("Combien de termes de Fibonacci veux-tu ?"))

fibo = []
a, b = 0, 1

for _ in range(n):
    fibo.append(a)
    a,b = b, a+b

print("Suite : ", fibo)

choisi = random.choice(fibo)
fact = math.factorial(choisi)

print(f"Factorielle : {fact}")

reponse = int(input("Quel terme a été choisi ? "))

if reponse == choisi :
    print("Bravo ")
else :
    print(f"Raté : {choisi}")