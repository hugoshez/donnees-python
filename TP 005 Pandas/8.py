import pandas as pd

# Charger le fichier de ventes dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Charger le fichier de promotions dans un DataFrame
df_promotions = pd.read_csv("donnees_promotions.csv")

# Effectuer une jointure entre df et df_promotions
df_merged = pd.merge(df, df_promotions, on=['Date', 'Magasin'], how='left')

# Afficher les premières lignes du DataFrame fusionné
print(df_merged.head())
