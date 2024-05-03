import matplotlib.pyplot as plt
import numpy as np

# Générer une série de 50 nombres allant de 0 à 10
x = np.linspace(0, 10, 50)

# Générer des données pour les deux séries (dans cet exemple, des carrés et des cubes des nombres x)
y1 = x ** 2
y2 = x ** 3

# Créer une nouvelle figure et des sous-graphiques
fig, (ax1, ax2) = plt.subplots(1, 2)

# Tracer les données dans le premier sous-graphique
ax1.plot(x, y1, '-o', color='blue', label='y = x^2')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Premier subplot')
ax1.legend()
ax1.grid(True)

# Tracer les données dans le deuxième sous-graphique
ax2.plot(x, y2, '--s', color='red', label='y = x^3')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Deuxième subplot')
ax2.legend()
ax2.grid(True)

# Ajuster la disposition pour éviter le chevauchement
plt.tight_layout()

# Sauvegarder le graphique en format PNG avec une résolution de 300 dpi
fig.savefig('graphique.png', dpi=300)

# Afficher la figure
plt.show()
