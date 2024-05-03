import matplotlib.pyplot as plt

# Catégories
categories = ['Catégorie 1', 'Catégorie 2', 'Catégorie 3', 'Catégorie 4', 'Catégorie 5']

# Nombre moyen d'articles vendus dans chaque catégorie
articles_vendus_moyen = [120, 190, 150, 210, 180]

# Incertitude associée à chaque moyenne
incertitude = [15, 20, 10, 25, 18]

# Créer un graphique à barres
plt.bar(categories, articles_vendus_moyen, color='skyblue', yerr=incertitude, capsize=5)

# Ajouter des étiquettes et un titre
plt.xlabel('Catégories')
plt.ylabel('Nombre moyen d\'articles vendus')
plt.title('Nombre moyen d\'articles vendus par catégorie avec incertitude')

# Afficher le graphique
plt.show()
