import matplotlib.pyplot as plt

# Catégories
categories = ['Catégorie 1', 'Catégorie 2', 'Catégorie 3', 'Catégorie 4', 'Catégorie 5']

# Nombre d'articles vendus dans chaque catégorie
articles_vendus = [120, 190, 150, 210, 180]

# Créer un graphique à barres
plt.bar(categories, articles_vendus, color='skyblue')

# Ajouter des étiquettes et un titre
plt.xlabel('Catégories')
plt.ylabel('Nombre d\'articles vendus')
plt.title('Nombre d\'articles vendus par catégorie')

# Afficher le graphique
plt.show()
