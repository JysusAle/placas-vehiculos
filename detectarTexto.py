import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np
import re
import csv
import datetime

def detectar_texto(placa):

    image = cv2.cvtColor(np.array(placa), cv2.COLOR_RGB2BGR)

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
        verificar_placa(text)

    # Mostrar imagen con resultados
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title('Texto detectado con EasyOCR')
    plt.show()

# Función para guardar la placa en un archivo CSV
def guardar_placa_en_csv(placa):
    with open('placas_detectadas.csv', mode='a', newline='') as file:
        hora_actual = datetime.datetime.now()
        writer = csv.writer(file)
        writer.writerow([hora_actual,placa])

# Función para verificar si el texto coincide con algún formato de placa
def verificar_placa(texto):
    patrones = {
        r"^[A-Z]{3}[-]\d{3}$",
        r"^[A-Z]{2}[-]\d{4}$",
        r"^[A-Z]{1}[-]\d{4}$",
        r"^[A-Z]{3}[-]\d{3}[-][A-Z]{1}$",
        r"^(CD|CC)[-]\d{3,4}$",
        r"^(OF|OFICIAL)[-]\d+$"
    }

    texto = texto.strip().upper()

    for patron in patrones:
        if re.match(patron, texto):
            guardar_placa_en_csv(texto)
            return True

    print("No coincide con ningún formato de placa conocido.")
    return False
