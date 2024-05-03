def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)
    

liste = [23, 27, 42, 63, 74]
resultat = calculate_average(liste)
print(f"La moyenne des nombres dans la liste est : {resultat}")