import numpy as np

# Définir la matrice 3x3
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculer les valeurs et vecteurs propres
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Afficher les résultats
print("Valeurs propres:")
print(eigenvalues)
print("\nVecteurs propres:")
print(eigenvectors)