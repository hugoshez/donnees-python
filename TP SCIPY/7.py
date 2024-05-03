import numpy as np
from scipy.stats import scoreatpercentile

# Tableau de valeurs
data = np.array([1, 2, 3, 4, 5])

# Calcul de la médiane (50ème percentile)
median = scoreatpercentile(data, 50)

print("50ème percentile:", median)