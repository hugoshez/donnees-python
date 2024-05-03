import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Créer des données pour la courbe sinusoïdale
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Initialiser la figure et les axes
fig, ax = plt.subplots()
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)

# Créer un point initial
point, = ax.plot([], [], marker='o', color='red')

# Fonction d'initialisation de l'animation
def init():
    point.set_data([], [])
    return point,

# Fonction d'animation
def update(frame):
    x_point = x[frame]
    y_point = y[frame]
    point.set_data(x_point, y_point)
    return point,

# Créer l'animation
ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True, interval=50)

# Afficher l'animation
plt.show()
