import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Générer des données aléatoires pour quatre variables
np.random.seed(0)
data = np.random.randn(100, 4)
df = pd.DataFrame(data, columns=['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4'])

# Tracer le pairplot avec Seaborn
sns.pairplot(df)

# Afficher le pairplot
plt.show()
