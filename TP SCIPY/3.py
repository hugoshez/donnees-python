import numpy as np
from scipy.ndimage import zoom

# Création d'une image de taille (10, 10) pour l'exemple
image = np.random.random((10, 10))

# Redimensionnement de l'image pour doubler sa taille
image_redimensionnee = zoom(image, 2)

# Affichage des tailles avant et après le redimensionnement
print(image_redimensionnee.shape)