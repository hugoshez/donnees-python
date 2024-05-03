import numpy as np
from scipy.ndimage import median_filter

# Création d'une image de taille (10, 10) pour l'exemple
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Redimensionnement de l'image pour doubler sa taille
filtered_arr = median_filter(arr, size=3)

# Affichage des tailles avant et après le redimensionnement
print(filtered_arr)