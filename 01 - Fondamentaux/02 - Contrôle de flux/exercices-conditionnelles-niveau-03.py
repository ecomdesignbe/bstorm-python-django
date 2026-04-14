# Demander à l'utilisateur de saisir le type de café (espresso, latte, cappuccino, etc.), la taille (petit, moyen, grand) 
# et le nombre de cafés qu’il désire.
# Calculer le coût total pour la commande en fonction du type et de la taille du café.
# Afficher les détails de la commande : ( type && taille && nombre && coût total )
# Offrir une réduction basée sur le montant total :
# 5% entre 20 et 50 || 10% entre 51 et 100 || 15% pour les montants supérieurs à 100

type_cafe = input("Type de café (espresso, latte, cappuccino) : ")
match type_cafe :
    case t if t == "espresso" : 
        cafe = "espresso"
        prix_cafe = 5    
    case t if t == "latte" : 
        cafe = "latte"
        prix_cafe = 10
    case t if t == "cappuccino" :
        cafe = "cappuccino"
        prix_cafe = 20
    case _:
        cafe = "Type de café inconnu"
        prix_cafe = 0

taille_cafe = input("Taille de café (petit, moyen, grand) : ")
match taille_cafe :
    case t if t == "petit" :
        taille = "petit"
        prix_taille = 5
    case t if t == "moyen" :
        taille = "moyen"
        prix_taille = 10
    case t if t == "grand" :
        taille = "grand"
        prix_taille = 20
    case _ : 
        taille = "Taille de café inconnue"
        prix_taille = 0

nbre_cafe = int(input("Nombre de café : "))

cout_total = (prix_cafe + prix_taille) * nbre_cafe

print(f'Voici le détail de votre commande : café: {cafe} / taille: {taille} / nombre: {nbre_cafe}')
print(f'Total : {cout_total} €')

if cout_total > 100 :
    reduction = int((cout_total * 15) / 100)
    total_reduc = int(cout_total - reduction)
    print(f'Total avec réduction: {cout_total} - {reduction} = {total_reduc} €')
elif cout_total >= 51 :
    reduction = int((cout_total * 10) / 100)
    total_reduc = int(cout_total - reduction)
    print(f'Total avec réduction: {cout_total} - {reduction} = {total_reduc} €')
elif cout_total >= 20 :
    reduction = int((cout_total * 5) / 100)
    total_reduc = int(cout_total - reduction)
    print(f'Total avec réduction: {cout_total} - {reduction} = {total_reduc} €')
else:
    print("pas de réduction")



