# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:37:15 2024

@author: pc
"""

import cv2
import torch

# Charger YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialisation de la caméra
cap = cv2.VideoCapture("road_video.mp4")  # Remplacez par 0 pour la webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Détection des objets
    results = model(frame)
    detections = results.pandas().xyxy[0]  # Résultats
    
    for _, row in detections.iterrows():
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        label = f"{row['name']} {row['confidence']:.2f}"
        color = (0, 255, 0) if row['name'] in ['car', 'truck', 'bus'] else (0, 0, 255)
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    cv2.imshow("Détection d'Objets", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
