import matplotlib.pyplot as plt

# Catégories d'articles vendus
categories = ['Catégorie 1', 'Catégorie 2', 'Catégorie 3', 'Catégorie 4', 'Catégorie 5']

# Proportions de ventes dans chaque catégorie
ventes = [20, 30, 15, 25, 10]

# Créer un graphique en camembert
plt.figure(figsize=(8, 8))  # Réglage de la taille de la figure
plt.pie(ventes, labels=categories, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)

# Ajouter un titre
plt.title('Proportion des ventes par catégorie')

# Afficher le graphique en camembert
plt.show()
