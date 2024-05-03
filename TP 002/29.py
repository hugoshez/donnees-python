livres = {
    "Le Petit Prince": "Antoine de Saint-Exupéry",
    "1984": "George Orwell",
    "Orgueil et Préjugés": "Jane Austen"
}

titre_livre = "Le Petit Prince"
auteur = livres.get(titre_livre)

if auteur:
    print(f"L'auteur du livre '{titre_livre}' est {auteur}.")
else:
    print(f"Le livre '{titre_livre}' n'existe pas dans le dictionnaire.")