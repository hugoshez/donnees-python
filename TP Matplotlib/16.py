import seaborn as sns
import matplotlib.pyplot as plt

# Exemple de données : trois groupes avec des valeurs aléatoires
import numpy as np
np.random.seed(0)
group1 = np.random.normal(0, 1, 100)
group2 = np.random.normal(1, 1.5, 100)
group3 = np.random.normal(2, 0.5, 100)

# Créer un dataframe pandas à partir des données
import pandas as pd
data = pd.DataFrame({'Group 1': group1, 'Group 2': group2, 'Group 3': group3})

# Tracer le boxplot avec Seaborn
sns.boxplot(data=data)

# Ajouter des étiquettes et un titre
plt.xlabel('Groupes')
plt.ylabel('Valeurs')
plt.title('Boxplot de la distribution des valeurs dans plusieurs groupes')

# Afficher le boxplot
plt.show()
