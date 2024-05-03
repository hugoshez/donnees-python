import datetime

def calculer_annee_naissance(age_actuel, age_utilisateur):
    annee_actuelle = datetime.date.today().year
    return annee_actuelle - age_utilisateur

nom = input("Entre ton nom : ")
age = int(input("Entre ton âge : "))
ville = input("Entre ta ville de résidence : ")

informations_utilisateur = {
    "nom": nom,
    "âge": age,
    "ville": ville
}

annee_naissance = calculer_annee_naissance(datetime.date.today().year, age)

message_personnalise = f"Bonjour {informations_utilisateur['nom']}, tu as {informations_utilisateur['âge']} ans, tu vie à {informations_utilisateur['ville']}"
print(f"{message_personnalise} et tu est né(e) en {annee_naissance}.")
