"""
Demande à l’utilisateur de saisir deux nombres, l’un entier et l’autre décimal, puis convertis-les
et affiche leur somme et leur produit.
"""
entier = int(input("Entre un entier : "))
reel = float(input("Entre un reel : "))

print(f"""
Somme = {entier + reel}
Produit = {entier * reel}
""")

"""
Déclare une variable contenant un mot et affiche sa longueur,
sa première lettre, sa dernière lettre et une partie du mot extraite par tranche
"""

mot = input("Entre un mot : ")

print(f"""
Longueur = {len(mot)}
1ère lettre = {mot[0]}
dernière lettre = {mot[-1]}
Tranche = {mot[1:4]}
""")