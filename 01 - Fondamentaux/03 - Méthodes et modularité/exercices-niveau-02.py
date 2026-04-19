# Crée une fonction saluer qui prend deux paramètres : prenom et age.
# Appelle-la en passant les arguments par position.
# Appelle-la à nouveau en passant les arguments par nom (dans un ordre différent).

def saluer(prenom, age):
    print(f'Bonjour {prenom}, tu as {age} ans')
    return saluer

saluer("steve",47)

saluer(age = 5, prenom = "Nathanael")