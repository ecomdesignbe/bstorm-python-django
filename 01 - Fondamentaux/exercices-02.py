# Demande à l’utilisateur de saisir son prénom puis affiche un message de salutation personnalisé.
# Demande à l’utilisateur de saisir son âge, convertis cette donnée en entier et affiche l’âge qu’il aura l’an prochain.

prenom = input("Quel est votre prenom ? ")

salutation = f"Bienvenue {prenom}"
print(salutation)

age = int(input("Quel est votre age ? "))

print(f"{salutation}, vous avez {age} ans et l'année prochaine vous aurez {age+1} ans")