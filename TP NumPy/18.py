import numpy as np

# Créer un tableau NumPy
arr = np.array([1, 2, 3, 4, 5])

# Définir le seuil
seuil = 3

# Remplacer les éléments supérieurs au seuil par 0
arr = np.where(arr > seuil, 0, arr)

# Afficher le tableau modifié
print(arr)