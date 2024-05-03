import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Générer des données aléatoires pour créer une matrice de corrélations
np.random.seed(0)
data = np.random.rand(10, 10)

# Calculer la matrice de corrélations
corr_matrix = np.corrcoef(data)

# Tracer le heatmap avec Seaborn
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# Ajouter un titre
plt.title('Heatmap de la matrice de corrélations')

# Afficher le heatmap
plt.show()
