# Crée un set contenant plusieurs fruits, dont certains en doublon.
# Affiche le set pour constater que les doublons ont disparu.
# Ajoute et supprime un fruit au set.

fruit = set(["banane", "banane", "pomme", "fraise"])

print(fruit)

fruit.add("orange")

print(fruit)

fruit.remove("banane")

print(fruit)