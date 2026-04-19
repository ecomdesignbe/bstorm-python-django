# Écris un programme qui demande à l’utilisateur deux nombres et affiche leur quotient.
# Si l’utilisateur saisit 0 comme dénominateur, intercepte l’erreur de division par zéro et affiche un message adapté.

nombre_a = int(input("Entrez le premier nombre : "))
nombre_b = int(input("Entrez le second nombre : "))

try:
    quotient = nombre_a / nombre_b
except ZeroDivisionError:
    print("Erreur : division par zéro interdite")
else:
    print("Succès, le résultat est", quotient)
