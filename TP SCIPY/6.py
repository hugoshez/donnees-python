import numpy as np
from scipy.stats import zscore

# Créer le tableau de valeurs
arr = np.array([1, 2, 3, 4, 5])

# Normaliser le tableau en utilisant la méthode z-score
normalized_arr = zscore(arr)

print(normalized_arr)