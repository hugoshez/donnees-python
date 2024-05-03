import numpy as np
from numpy import roots

# Coefficients du polynôme
coefficients = [1, -4, 4]

# Calcul des racines
racines = roots(coefficients)

# Affichage des racines
print("Les racines du polynôme sont :", racines)