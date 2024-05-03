import pandas as pd

# Chargez le fichier dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Affichez les premières lignes du DataFrame pour vérification
print(df.head(5))

# Afficher le nombre de lignes et de colonnes du DataFrame
nombre_lignes, nombre_colonnes = df.shape
print("Nombre de lignes :", nombre_lignes)
print("Nombre de colonnes :", nombre_colonnes)

# Afficher le type de chaque colonne
print(df.dtypes)
