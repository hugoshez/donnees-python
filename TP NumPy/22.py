import numpy as np

# Définir la matrice 3x3
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculer le déterminant
determinant = np.linalg.det(matrix)

# Afficher le résultat
print("Le déterminant de la matrice est :", determinant)