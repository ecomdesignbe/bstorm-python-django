# Créer un jeu où l'utilisateur doit deviner un nombre aléatoire entre 1 et 10. L'utilisateur a 5 tentatives pour trouver le nombre.

random_number = 9
game = 0
max_game = 5

while game < max_game : 
    prompt_number = int(input("Entrer un nombre entre 0 et 10 : "))
    if random_number == prompt_number:
        print("Bravo c'est le bon nombre")
        break
    else:
        game += 1
        if game < max_game:
            print(f"Raté ! Il te reste {max_game - game} tentative(s).")
        else:
            print(f"Perdu ! Le bon nombre était {random_number}.")


