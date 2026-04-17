"""
Créer un jeu où l'utilisateur doit deviner un nombre aléatoire entre 1 et 10.
L'utilisateur a 5 tentatives pour trouver le nombre.
"""

import random

secret = random.randint(1, 10)
tentatives = 5

for essai in range(1, tentatives + 1):
    proposition = int(input(f"Tentative {essai}/5 - Devine le nombre : "))

    if proposition == secret:
        print("Bravo, tu as trouvé !")
        break
    elif proposition < secret:
        print("Trop petit !")
    else:
        print("Trop grand !")
else:
    print(f"Perdu ! Le nombre était {secret} ! ")