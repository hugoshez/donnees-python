import matplotlib.pyplot as plt
import numpy as np

# Générer une série de 50 nombres allant de 0 à 10
x = np.linspace(0, 10, 50)

# Générer des données pour les deux séries (dans cet exemple, des carrés et des cubes des nombres x)
y1 = x ** 2
y2 = x ** 3

# Tracer le graphique avec deux séries de données et des styles de ligne différents
plt.plot(x, y1, '-o', color='blue', label='y = x^2')  # style de ligne '-o' et couleur bleue
plt.plot(x, y2, '--s', color='red', label='y = x^3')  # style de ligne '--s' et couleur rouge
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graphique de deux séries de données')
plt.grid(True)  # Activer la grille
plt.show()
