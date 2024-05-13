import cv2

# Charger le modèle de détection de visages pré-entraîné
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Charger l'image où détecter les visages
img = cv2.imread('visage.jpg')

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Détecter les visages
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Dessiner des rectangles autour des visages détectés
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Afficher l'image avec les visages détectés
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
