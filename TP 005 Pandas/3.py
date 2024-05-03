import pandas as pd

# Chargez le fichier dans un DataFrame
df = pd.read_csv("donnees_ventes_tp_pandas.csv")

# Vérifier les valeurs manquantes
print("Nombre de valeurs manquantes par colonne :\n", df.isnull().sum())

# Traiter les valeurs manquantes si nécessaire
# Exemple : Remplacer les valeurs manquantes par la moyenne de la colonne
# df.fillna(df.mean(), inplace=True)

# Supprimer les lignes dupliquées
df.drop_duplicates(inplace=True)