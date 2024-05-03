import matplotlib.pyplot as plt
import numpy as np

# Générer deux séries de 100 points chacune suivant une distribution normale
x = np.random.normal(loc=0, scale=1, size=100)
y = np.random.normal(loc=0, scale=1, size=100)

# Créer un graphique de dispersion
plt.scatter(x, y, color='orange', alpha=0.7)

# Ajouter des étiquettes et un titre
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graphique de dispersion de deux séries de données')

# Afficher le graphique
plt.show()
