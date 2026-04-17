"""
Écrire un programme pour trouver la plus longue suite palindromique dans
une chaîne de caractères donnée par l'utilisateur.
"""

texte = input("Entre une chaîne : ").lower()

plus_long = ""

for i in range(len(texte)):
    for j in range(i+1, len(texte) + 1):
        morceau = texte[i:j]

        if morceau == morceau[::-1] and len(morceau) > len(plus_long):
            plus_long = morceau

print("La plus longue chaine palindromique : ", plus_long)