"""
Demande à l’utilisateur de saisir son prénom puis affiche un message
de salutation personnalisé.
"""
prenom = input("Quel est ton prénom ?")
print(f"Bonjour {prenom} !")

"""
Demande à l’utilisateur de saisir son âge, convertis cette donnée en entier
et affiche l’âge qu’il aura l’an prochain.
"""

age = int(input("Quel âge as-tu ?"))
print(f"L'an prochain, j'aurai {age + 1} ans !")
