import pandas as pd

# Charger le fichier dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Calculer le revenu en multipliant la quantité vendue par le prix unitaire
df['Revenu'] = df['Quantité vendue'] * df['Prix unitaire']

# Calculer le total des revenus par magasin
revenus_par_magasin = df.groupby('Magasin')['Revenu'].sum()

# Trouver le produit le plus vendu
produit_plus_vendu = df.groupby('Produit')['Quantité vendue'].sum().idxmax()

# Afficher le total des revenus par magasin
print("Total des revenus par magasin :\n", revenus_par_magasin)

# Afficher le produit le plus vendu
print("\nProduit le plus vendu :", produit_plus_vendu)
