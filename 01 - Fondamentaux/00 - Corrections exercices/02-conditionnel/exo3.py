"""
Demander à l'utilisateur de saisir le type de café
(espresso, latte, cappuccino, etc.), la taille (petit, moyen, grand)
et le nombre de cafés qu’il désire.

Calculer le coût total pour la commande en fonction du type
et de la taille du café.
Afficher les détails de la commande :
( type && taille && nombre && coût total )

Offrir une réduction basée sur le montant total :
5% entre 20 et 50 || 10% entre 51 et 100 || 15% pour
les montants supérieurs à 100
"""

type_cafe = input(f"""
Type de café :
    Espresso
    Latte
    Cappuccino
""").lower()

taille_cafe = input(f"""
Taille de café :
    Petit
    Moyen
    Grand
""").lower()

quantite_cafe = int(input("Nombre de café : "))

prix_cafe = {
    "espresso" : { "petit": 2.0, "moyen": 2.5, "grand": 12.0},
    "latte": {"petit": 3.0, "moyen": 3.5, "grand": 12.0},
    "cappuccino": {"petit": 3.0, "moyen": 3.5, "grand": 12.0}
}

if type_cafe in prix_cafe and taille_cafe in prix_cafe[type_cafe]:
    total = prix_cafe[type_cafe][taille_cafe] * quantite_cafe

    reduction = 0

    if 20 <= total <= 50:
        reduction = 0.05
    elif 51 <= total <= 100:
        reduction = 0.10
    elif total > 100:
        reduction = 0.15

    total_final = total * (1 - reduction)

    print(f"""
################## COMMANDE ################## 
Type: {type_cafe}
Taille: {taille_cafe}
Quantité: {quantite_cafe}
Total avant réduction: {total} euros
Réduction: {reduction* 100}%
Total après réduction: {total_final} euros
""")
