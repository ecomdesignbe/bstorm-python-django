#Demander à l'utilisateur de saisir une note entre 0 et 100 et utiliser la structure if-else pour 
# classifier la note en différentes catégories. ( Exemple : entre 0 & 10 : ridicule )

note = int(input("Entrez votre note ? "))

if note == 100 :
    print("Extraordinaire")
elif note >= 90:
    print("Excellent")
elif note >= 80:
    print("Genial")
elif note >= 70:
    print("Top")
elif note >= 60:
    print("Bravo")
elif note >= 50:
    print("Tout juste")
elif note >= 40:
    print("On repassera")
elif note >= 30:
    print("What the f***")
elif note >= 20:
    print("Pénible")
elif note >= 10:
    print("A l'année prochaine")
else :
    print("Ridicule")


