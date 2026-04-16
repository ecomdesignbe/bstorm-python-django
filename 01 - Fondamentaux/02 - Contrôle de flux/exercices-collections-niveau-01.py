# Crée une liste contenant trois prénoms.
# Affiche le premier et le dernier prénom.
# Ajoute un nouveau prénom à la fin de la liste.
# Remplace le deuxième prénom par un autre.

prenom = ["Steve", "Nathanaël", "Mélanie"] 

print(prenom[0], prenom[2])
prenom.append("Gizmo")

print(prenom)

prenom[1] = "Thunder"
print(prenom)
