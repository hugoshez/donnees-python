import scipy.io

# Charger le fichier .mat
data = scipy.io.loadmat('data.mat')

# Accéder aux variables x et y
x = data['x']
y = data['y']

# Afficher les variables
print("Variable x :\n", x)
print("Variable y :\n", y)
