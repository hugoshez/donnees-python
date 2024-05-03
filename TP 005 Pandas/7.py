import pandas as pd

# Charger le fichier dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Calculer le revenu en multipliant la quantité vendue par le prix unitaire
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire']

# Calculer le revenu total par magasin
revenu_total_par_magasin = df.groupby('Magasin')['Revenu'].sum()

# Afficher le revenu total par magasin
print("Revenu total par magasin :\n", revenu_total_par_magasin)

# Triez le DataFrame par date de vente en ordre décroissant
df = df.sort_values(by='Date', ascending=False)

# Triez les magasins selon le revenu total en ordre décroissant
df = df.groupby('Magasin').sum().sort_values(by='Revenu', ascending=False)

print(df)
