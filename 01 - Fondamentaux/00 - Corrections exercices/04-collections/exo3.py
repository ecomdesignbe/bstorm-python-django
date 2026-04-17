"""
Crée un set contenant plusieurs fruits, dont certains en doublon.
Affiche le set pour constater que les doublons ont disparu.
Ajoute et supprime un fruit au set.
"""

fruits = {"pommes", "banane", "orange", "orange"}

print(fruits)

fruits.add("kiwi")
fruits.remove("banane")

print(fruits)
