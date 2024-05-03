import matplotlib.pyplot as plt
import numpy as np

# Générer 100 valeurs aléatoires tirées d'une distribution normale
data = np.random.normal(loc=0, scale=1, size=100)

# Créer un histogramme
plt.hist(data, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.title('Histogramme de la distribution normale')
plt.grid(True)

# Afficher l'histogramme
plt.show()
