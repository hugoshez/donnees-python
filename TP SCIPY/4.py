import numpy as np
from scipy.stats import norm

# Définir les paramètres de la distribution normale
mean = 0  # Moyenne
std = 1  # Écart-type

# Générer une matrice 3x3 de nombres aléatoires tirés d'une distribution normale
matrix = norm.rvs(loc=mean, scale=std, size=(3, 3))

print(matrix)