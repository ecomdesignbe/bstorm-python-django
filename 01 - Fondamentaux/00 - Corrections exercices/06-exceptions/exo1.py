"""
Écris un programme qui demande à l’utilisateur deux nombres
et affiche leur quotient.

Si l’utilisateur saisit 0 comme dénominateur,
intercepte l’erreur de division par zéro et affiche un message adapté.
"""

try:
    a = float(input("Numérateur :"))
    b = float(input("Dénominateur :"))
    print("Quotient : ", a/b)
except ZeroDivisionError:
    print("Erreur, division par 0")
