import matplotlib.pyplot as plt
import numpy as np

# Générer une série de 50 nombres allant de 0 à 10
x = np.linspace(0, 10, 50)

# Générer des données pour l'axe des ordonnées (dans cet exemple, des carrés des nombres x)
y = x ** 2

# Tracer le graphique de ligne avec une couleur rouge
plt.plot(x, y, '-o', color='red', label='y = x^2')  # '-o' pour spécifier le style de ligne et de marqueurs
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graphique de ligne')
plt.grid(True)  # Activer la grille
plt.show()
