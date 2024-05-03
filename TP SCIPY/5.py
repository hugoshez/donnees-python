from scipy.spatial.distance import euclidean

# Coordonnées des points
point1 = (1, 2) 
point2 = (4, 6) 

# Calcul de la distance euclidienne entre les deux points
distance = euclidean(point1, point2)

print("La distance euclidienne entre les points", point1, "et", point2, "est", distance)