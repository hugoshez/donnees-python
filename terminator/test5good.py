import cv2
import torch
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weights
from PIL import Image, ImageDraw, ImageFont
import numpy as np

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

# Charger le modèle pré-entraîné
model = fasterrcnn_resnet50_fpn(weights=FasterRCNN_ResNet50_FPN_Weights.DEFAULT)
model.eval()  # Mode évaluation

# Définir les transformations
transform = T.Compose([T.ToTensor()])

# Ouvrir la vidéo
cap = cv2.VideoCapture('test20.mp4')

# Paramètres de sortie pour la vidéo annotée
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('test20_output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# Définir une police pour le texte
font_path = "C:\\Windows\\Fonts\\arial.ttf"
font = ImageFont.truetype(font_path, 24)

# Dictionnaire pour maintenir les labels visibles pendant plusieurs frames
visible_labels = {}

# Lire chaque frame de la vidéo
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir l'image BGR en RGB et appliquer un filtre rouge
    image = Image.fromarray(frame[:, :, ::-1])
    r, g, b = image.split()
    r = r.point(lambda i: i * 0.05)  # Augmenter le rouge
    g = g.point(lambda i: i * 1.2)  # Réduire légèrement le vert
    b = b.point(lambda i: i * 0.05)  # Réduire légèrement le bleu
    image = Image.merge('RGB', (r, g, b))

    # Appliquer les transformations
    image_tensor = transform(image)

    # Détecter les objets
    with torch.no_grad():
        prediction = model([image_tensor])

    # Dessiner les boîtes et les labels sur l'image
    draw = ImageDraw.Draw(image)
    for i, (box, label, score) in enumerate(zip(prediction[0]['boxes'], prediction[0]['labels'], prediction[0]['scores'])):
        if score > 0.5:
            label_index = label.item()
            if label_index >= len(COCO_INSTANCE_CATEGORY_NAMES):
                print(f"Label index {label_index} out of range.")
                continue
            label_name = COCO_INSTANCE_CATEGORY_NAMES[label_index]
            box = box.tolist()
            draw.rectangle([(box[0], box[1]), (box[2], box[3])], outline='white', width=3)
            draw.text((box[0], box[1] - 10), label_name, fill='white', font=font)

    # Convertir PIL Image en array NumPy pour l'écrire avec OpenCV
    frame_annotated = np.array(image)
    frame_annotated = frame_annotated[:, :, ::-1]  # Convertir RGB en BGR pour OpenCV

    # Écrire la frame annotée dans la nouvelle vidéo
    out.write(frame_annotated)

# Relâcher les ressources
cap.release()
out.release()

print("Video processing complete. The output video is saved as 'output_video10.mp4'")
