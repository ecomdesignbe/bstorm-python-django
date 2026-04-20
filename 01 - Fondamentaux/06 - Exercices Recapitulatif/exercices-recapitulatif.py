# Exercice récapitulatif – Gestion d’une petite bibliothèque 
# On veut écrire un petit programme qui gère les livres d’une bibliothèque.
# Le programme doit fonctionner en mode console et rester actif tant que l’utilisateur n’a pas choisi de l’arrêter.
# Étapes à réaliser
# 1. Gestion de données :
# Créer un fichier sous un format choisi personnellement (json,...) pour persister vos données.
# Créer une liste de dictionnaires qui représente vos données et le populer.
# 
# 2. Fonctions à écrire :
# afficher_bibliotheque(biblio) → affiche tous les livres et leur état (disponible ou emprunté).
# rechercher_livre(biblio, titre) → cherche un livre par son titre. Si le livre n’existe pas, afficher un message d’erreur.
# emprunter_livre(biblio, titre) → change "disponible" en False si le livre est trouvé et disponible.
# retourner_livre(biblio, titre) → remet "disponible" à True si le livre est trouvé.
# compter_livres(biblio) → retourne le nombre total de livres et le nombre disponibles.
# 
# 3. Boucle principale (menu)
# Le programme doit tourner en boucle et proposer à l’utilisateur un menu avec les différentes options liées aux fonctions et
# offrir une option statistiques, suggestion de lecture aléatoire et quitter.
# Tant que l’utilisateur ne choisit pas stop, le programme continue à tourner.
# 4. Tips & tricks
# Utiliser le module random pour proposer la suggestion de lecture aléatoire (option 6).
# Gérer les erreurs de saisie (exemple : si l’utilisateur tape du texte au lieu d’un nombre).

import json              # Permet de lire/écrire dans un fichier JSON
import random            # Permet de choisir un élément aléatoire

FICHIER = r"01 - Fondamentaux\06 - Exercices Recapitulatif\bibliotheque.json"   # Nom du fichier de stockage


# Fonction pour charger la bibliothèque depuis le fichier
def charger_biblio():
    try:
        with open(FICHIER, "r") as f:   # Ouvre le fichier en lecture
            return json.load(f)         # Convertit le JSON en liste Python
    except FileNotFoundError:           # Si le fichier n'existe pas
        return []                       # Retourne une liste vide


# Fonction pour sauvegarder la bibliothèque dans le fichier
def sauvegarder_biblio(biblio):
    with open(FICHIER, "w") as f:       # Ouvre le fichier en écriture
        json.dump(biblio, f, indent=4)  # Écrit les données en format JSON


# Affiche tous les livres
def afficher_bibliotheque(biblio):
    if not biblio:                      # Vérifie si la liste est vide
        print("📚 Bibliothèque vide.")
        return                          # Quitte la fonction

    for livre in biblio:                # Parcourt chaque livre
        # Condition : si disponible → "Disponible", sinon → "Emprunté"
        etat = "Disponible" if livre["disponible"] else "Emprunté"
        
        # Affiche les infos du livre
        print(f"- {livre['titre']} ({livre['auteur']}) : {etat}")


# Recherche un livre par titre
def rechercher_livre(biblio, titre):
    for livre in biblio:                            # Parcourt les livres
        if livre["titre"].lower() == titre.lower(): # Compare sans majuscules
            print("Livre trouvé :", livre)
            return livre                            # Retourne le livre trouvé

    print("❌ Livre non trouvé.")                   # Si aucun trouvé
    return None


# Emprunter un livre
def emprunter_livre(biblio, titre):
    livre = rechercher_livre(biblio, titre)  # Cherche le livre

    if livre:                                # Vérifie qu'il existe
        if livre["disponible"]:              # S'il est disponible
            livre["disponible"] = False      # Devient emprunté
            print("✅ Livre emprunté.")
        else:
            print("⚠️ Livre déjà emprunté.") # Déjà pris


# Retourner un livre
def retourner_livre(biblio, titre):
    livre = rechercher_livre(biblio, titre)  # Cherche le livre

    if livre:                                # Vérifie qu'il existe
        if not livre["disponible"]:          # S'il est emprunté
            livre["disponible"] = True       # Devient disponible
            print("✅ Livre retourné.")
        else:
            print("⚠️ Livre déjà disponible.")


# Compter les livres
def compter_livres(biblio):
    total = len(biblio)   # Nombre total de livres

    # Compte les livres disponibles (True)
    dispo = sum(1 for livre in biblio if livre["disponible"])

    print(f"📊 Total : {total} | Disponibles : {dispo}")


# Suggestion de livre aléatoire
def suggestion_aleatoire(biblio):
    # Liste des livres disponibles uniquement
    dispos = [livre for livre in biblio if livre["disponible"]]

    if dispos:                                 # S'il y en a au moins un
        livre = random.choice(dispos)           # Choix aléatoire
        print(f"📖 Suggestion : {livre['titre']} de {livre['auteur']}")
    else:
        print("❌ Aucun livre disponible.")


# Menu principal
def menu():
    biblio = charger_biblio()   # Charge les données au démarrage

    while True:                 # Boucle infinie (programme actif)
        print("\n--- MENU ---")
        print("1. Afficher la bibliothèque")
        print("2. Rechercher un livre")
        print("3. Emprunter un livre")
        print("4. Retourner un livre")
        print("5. Statistiques")
        print("6. Suggestion aléatoire")
        print("7. Quitter")

        try:
            # Demande un choix et convertit en entier
            choix = int(input("Votre choix : "))
        except ValueError:
            # Si l'utilisateur n'entre pas un nombre
            print("❌ Veuillez entrer un nombre.")
            continue              # Recommence la boucle

        if choix == 1:
            afficher_bibliotheque(biblio)

        elif choix == 2:
            titre = input("Titre du livre : ")
            rechercher_livre(biblio, titre)

        elif choix == 3:
            titre = input("Titre du livre : ")
            emprunter_livre(biblio, titre)

        elif choix == 4:
            titre = input("Titre du livre : ")
            retourner_livre(biblio, titre)

        elif choix == 5:
            compter_livres(biblio)

        elif choix == 6:
            suggestion_aleatoire(biblio)

        elif choix == 7:
            sauvegarder_biblio(biblio)  # Sauvegarde avant quitter
            print("👋 Au revoir !")
            break                       # Quitte la boucle

        else:
            print("❌ Choix invalide.") # Si numéro incorrect


# Lance le programme
menu()

