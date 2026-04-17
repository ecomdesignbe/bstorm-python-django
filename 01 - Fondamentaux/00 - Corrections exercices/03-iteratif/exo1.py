"""
Créer une boucle while, une boucle do … while et une boucle for.
Dans chaque boucle, utilisez la sortie console (print) et affichez un compteur de l’itération en cours
"""

print("While")
i = 0

while i < 5:
    print(f"Itération {i}")
    i += 1

print("Do while")
i = 0

while True:
    print(f"Itération {i}")
    i += 1

    if i >= 5:
        break

print("For")
for i in range(5):
    print(f"Itération {i}")