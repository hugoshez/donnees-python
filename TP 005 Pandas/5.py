import pandas as pd

# Charger le fichier dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Convertir la colonne Date en type datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sélectionner les données des ventes qui ont eu lieu en 2022
ventes_2022 = df[df['Date'].dt.year == 2022]

# Filtrer les données pour afficher uniquement les ventes où plus de 100 articles ont été vendus
ventes_plus_100_articles = df[df['Quantité vendue'] > 100]

# Afficher les premières lignes des ventes en 2022
print("Ventes en 2022 :\n", ventes_2022.head())

# Afficher les premières lignes des ventes avec plus de 100 articles vendus
print("\nVentes avec plus de 100 articles vendus :\n", ventes_plus_100_articles.head())
