import easyocr
import cv2
import matplotlib.pyplot as plt
import time

def detectar_texto():
    time.sleep(2)
    # Cargar imagen recortada
    image_path = 'placa_recortada.jpg'
    image = cv2.imread(image_path)

    # Inicializar lector de EasyOCR
    reader = easyocr.Reader(['es', 'en'])

    # Ejecutar OCR
    results = reader.readtext(image)

    # Mostrar resultados
    for (bbox, text, prob) in results:
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(image, text, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        print(f"Texto detectado: '{text}' con confianza {prob:.2f}")

    # Mostrar imagen con resultados
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title('Texto detectado con EasyOCR')
    plt.show()

detectar_texto()