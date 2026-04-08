# Vérifie et affiche le résultat de la conversion en booléen de différentes valeurs :
# un nombre nul, un nombre non nul, une chaîne vide et une chaîne contenant du texte.
nbr_nul = 0
nbr_non_nul = 22
chaine_vide = ''
chaine_txt = "Ceci est une chaine avec du texte"
print(f"Ceci verifie et affiche le résultat de la conversion en booleen d'un nombre nul = {nbr_nul} = {bool(nbr_nul)}")
print(f"Ceci verifie et affiche le résultat de la conversion en booleen d'un nombre non nul = {nbr_non_nul} = {bool(nbr_non_nul)}")
print(f"Ceci verifie et affiche le résultat de la conversion en booleen d'une chaîne vide = {chaine_vide} = {bool(chaine_vide)}")
print(f"Ceci verifie et affiche le résultat de la conversion en booleen d'une chaîne contenant du texte = {chaine_txt} = {bool(chaine_txt)}")

