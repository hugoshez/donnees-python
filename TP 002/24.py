def pair_ou_impair(nombre):
    if nombre % 2 == 0:
        return "pair"
    else:
        return "impair"

nombre = 7
resultat = pair_ou_impair(nombre)
print(f"Le nombre {nombre} est {resultat}.")