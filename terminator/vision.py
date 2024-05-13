import torch
import cv2
import numpy as np
from torchvision.models.detection import fasterrcnn_resnet50_fpn


# Liste des catégories COCO (s'assurer qu'elle est complète)
COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle',
    'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
    'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
    'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
    'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
    'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard',
    'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
    'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
    'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
    'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
    'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
    'teddy bear', 'hair drier', 'toothbrush'
]

# Charger le modèle Faster R-CNN pré-entraîné sur COCO
model = fasterrcnn_resnet50_fpn(pretrained=True)
# Mettre le modèle en mode évaluation
model.eval()

# Ouvrir la vidéo à l'aide d'OpenCV
cap = cv2.VideoCapture('djadjadinaz.mp4')

# Paramètres de sortie pour la vidéo annotée
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('djadjadinaz.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))


# Vérifier si la vidéo est ouverte avec succès
if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la vidéo")
    exit()

# Lire la vidéo frame par frame
while cap.isOpened():
    # Lire une frame
    ret, frame = cap.read()
    # Vérifier si la lecture de la frame a réussi
    if not ret:
        break

    # Convertir la frame de BGR à RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convertir la frame de RGB à HSV
    hsv_frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2HSV)

    # Modifier la composante de teinte pour changer la couleur
    # Par exemple, changer la teinte à 120 pour rendre la vidéo de couleur verte
    hsv_frame[:, :, 0] = 120

    # Convertir la frame de HSV à RGB
    modified_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2RGB)

    # Ajouter un filtre rouge à la frame
    red_frame = cv2.addWeighted(frame, 1, np.zeros_like(frame), 0, 0)

    # Ajouter les écritures comme la vision de Terminator
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(red_frame, 'TARGET ACQUIRED', (50, 50), font, 1, (0, 0, 255), 2)

    # Afficher la frame
    cv2.imshow('Video', red_frame)
    out.write(red_frame) # Écriture de la frame modifiée dans la vidéo de sortie


    # Attendre 25 millisecondes (40 FPS)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
out.release()
cv2.destroyAllWindows()
