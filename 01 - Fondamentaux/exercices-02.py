prenom = input("Quel est votre prenom ? ")

salutation = f"Bienvenue {prenom}"
print(salutation)

age = input("Quel est votre age ? ")
age = int(age)

print(f"{salutation}, vous avez {age} ans et l'année prochaine vous aurez {age+1} ans")