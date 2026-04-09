# Demande à l’utilisateur de saisir deux nombres, l’un entier et l’autre décimal, 
# puis convertis-les et affiche leur somme et leur produit.

nbr_a = int(input("Entrez un nombre entier "))
nbr_b = int(input("Entrez un nombre décimal "))

somme = nbr_a + nbr_b
produit = nbr_a * nbr_b

print(f"Voici la somme de tes 2 nombres = {nbr_a} + {nbr_b} = {somme}")
print(f"Voici le produit de tes 2 nombres = {nbr_a} * {nbr_b} = {produit}")

############################################################################

# Déclare une variable contenant un mot et affiche sa longueur, sa première lettre, sa dernière lettre 
# et une partie du mot extraite par tranche.

mot = "MayTheForceBeWithYou"
print(f"Dans votre mot : {mot}, il y a {len(mot)} lettres")
print(f"La premiere lettre est {mot[1]}")
print(f"La dernière lettre est {mot[-1]}")
print(f"Une partie extraite est {mot[3:]}")