import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Définir la fonction z = f(x, y)
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Créer des données pour les variables x et y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = f(x, y)

# Créer une figure 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer la surface
surf = ax.plot_surface(x, y, z, cmap='viridis')

# Ajouter une barre de couleur
fig.colorbar(surf)

# Ajouter des étiquettes d'axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Ajouter un titre
ax.set_title('Surface 3D de z = f(x, y)')

# Afficher le graphique
plt.show()
