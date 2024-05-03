import matplotlib.pyplot as plt
import numpy as np

# Temps
temps = np.arange(1, 11)  # Par exemple, 10 points de données

# Données pour les trois groupes
groupe1 = np.random.randint(1, 10, size=len(temps))
groupe2 = np.random.randint(1, 10, size=len(temps))
groupe3 = np.random.randint(1, 10, size=len(temps))

# Créer un graphique à empilement
plt.stackplot(temps, groupe1, groupe2, groupe3, labels=['Groupe 1', 'Groupe 2', 'Groupe 3'])

# Ajouter des étiquettes et un titre
plt.xlabel('Temps')
plt.ylabel('Valeurs')
plt.title('Évolution des trois groupes avec le temps')
plt.legend()

# Afficher le graphique
plt.show()
