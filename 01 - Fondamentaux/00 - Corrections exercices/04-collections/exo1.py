"""
Crée une liste contenant trois prénoms.
Affiche le premier et le dernier prénom.
Ajoute un nouveau prénom à la fin de la liste.
Remplace le deuxième prénom par un autre
"""

prenoms = ["Steve", "Romane", "Fabian"]

print(f"1er prénom : {prenoms[0]}")
print(f"dernier prénom : {prenoms[-1]}")

prenoms.append("Marie-Christine")
prenoms[1] = "Lorenzo"
print(prenoms)
