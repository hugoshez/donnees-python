import matplotlib.pyplot as plt
import numpy as np

# Créer des données pour les 4 distributions
data1 = np.random.normal(loc=0, scale=1, size=1000)
data2 = np.random.normal(loc=2, scale=1.5, size=1000)
data3 = np.random.uniform(low=-1, high=1, size=1000)
data4 = np.random.exponential(scale=1, size=1000)

# Créer une figure et des sous-graphiques
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Tracer les données sur chaque sous-graphique
axs[0, 0].hist(data1, bins=30, color='blue', alpha=0.7)
axs[0, 0].set_title('Distribution normale')

axs[0, 1].hist(data2, bins=30, color='red', alpha=0.7)
axs[0, 1].set_title('Distribution normale (2, 1.5)')

axs[1, 0].hist(data3, bins=30, color='green', alpha=0.7)
axs[1, 0].set_title('Distribution uniforme')

axs[1, 1].hist(data4, bins=30, color='purple', alpha=0.7)
axs[1, 1].set_title('Distribution exponentielle')

# Ajuster l'espacement entre les sous-graphiques
plt.tight_layout()

# Afficher la figure
plt.show()
