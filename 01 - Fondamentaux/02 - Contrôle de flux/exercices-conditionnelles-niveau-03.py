# Demander à l'utilisateur de saisir le type de café (espresso, latte, cappuccino, etc.), la taille (petit, moyen, grand) 
# et le nombre de cafés qu’il désire.
# Calculer le coût total pour la commande en fonction du type et de la taille du café.
# Afficher les détails de la commande : ( type && taille && nombre && coût total )
# Offrir une réduction basée sur le montant total :
# 5% entre 20 et 50 || 10% entre 51 et 100 || 15% pour les montants supérieurs à 100

type_cafe = input("Type de café (espresso, latte, cappuccino) : ")

match type_cafe:
    case "espresso":
        prix_cafe = 5
    case "latte":
        prix_cafe = 10
    case "cappuccino":
        prix_cafe = 20
    case _:
        print("Type de café invalide")
        prix_cafe = 0

taille_cafe = input("Taille de café (petit, moyen, grand) : ")

match taille_cafe:
    case "petit":
        prix_taille = 5
    case "moyen":
        prix_taille = 10
    case "grand":
        prix_taille = 20
    case _:
        print("Taille invalide")
        prix_taille = 0

nbre_cafe = int(input("Nombre de café : "))

cout_total = (prix_cafe + prix_taille) * nbre_cafe

print("\nCommande :", type_cafe, "/", taille_cafe, "/ x", nbre_cafe)
print("Total avant réduction :", cout_total, "€")

# Réduction
reduction = 0

if cout_total > 100:
    reduction = 0.15
elif cout_total >= 51:
    reduction = 0.10
elif cout_total >= 20:
    reduction = 0.05

total_final = cout_total - (cout_total * reduction)

if reduction > 0:
    print("Réduction :", reduction * 100, "%")
    print("Total après réduction :", total_final, "€")
else:
    print("Pas de réduction")


