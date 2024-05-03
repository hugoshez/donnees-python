import numpy as np
from numpy import matmul

# Définition des matrices A et B
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

# Multiplication des matrices A et B
result = matmul(A, B)

print("Résultat de la multiplication des matrices A et B :")
print(result)