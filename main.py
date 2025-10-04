import torch
from PIL import Image
import matplotlib.pyplot as plt
import easyocr
import cv2
from detectarTexto import detectar_texto

# Cargar modelo YOLOv5 personalizado
model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt',force_reload=True, source='local')

# Cargar imagen original
img = Image.open('imagenes-prueba/img2.jpg')

# Detectar objetos
results = model(img)
results.print()
results.save()

# Obtener resultados como DataFrame
df = results.pandas().xyxy[0]
print(df)


# Verificar si hay detecciones
if len(df) > 0:
    # Tomar la primera detección
    x1, y1, x2, y2 = df.iloc[0][['xmin', 'ymin', 'xmax', 'ymax']].astype(int)

    # Recortar la región de la placa
    plate_img = img.crop((x1, y1, x2, y2))
    plate_img.save("placa_recortada.jpg")

    print("TERMINA SCRIPT 1")
    detectar_texto(plate_img)

else:
    print("No se detectó ninguna placa en la imagen.")