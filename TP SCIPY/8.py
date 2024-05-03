import numpy as np

# Créer le tableau
arr = np.array([10, 20, 30, 40, 50])

# Trouver la valeur minimale et son indice
min_value = np.min(arr)
min_index = np.argmin(arr)

# Trouver la valeur maximale et son indice
max_value = np.max(arr)
max_index = np.argmax(arr)

# Afficher les résultats
print("Valeur minimale :", min_value)
print("Valeur maximale :", max_value)
