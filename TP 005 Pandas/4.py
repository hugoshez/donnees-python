import pandas as pd

# Chargez le fichier dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Calculer la colonne Revenu
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire']

# Créer la colonne Année
df['Année'] = pd.to_datetime(df['Date']).dt.year

# Afficher le DataFrame avec les nouvelles colonnes
print(df.head())
