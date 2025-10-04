# 🚘 Detector de Placas Mexicanas con YOLOv5 + EasyOCR

Este proyecto detecta **placas vehiculares mexicanas** en imágenes y realiza reconocimiento de texto (OCR) para extraer y verificar los caracteres utilizando **YOLOv5** y **EasyOCR**.  
El código fue desarrollado y probado en **Linux**, pero puede adaptarse a otros sistemas operativos.

---

## 🧠 Descripción general

El flujo del programa es el siguiente:

1. **`main.py`** carga un modelo YOLOv5 previamente entrenado para localizar la placa en una imagen.
2. Se recorta la región detectada (la placa).
3. Se pasa la placa recortada al módulo **`detectarTexto.py`**, que usa **EasyOCR** para reconocer los caracteres.
4. Se valida si el texto reconocido coincide con un formato de placa mexicana.
5. Si coincide, se guarda la placa detectada en el archivo `placas_detectadas.csv` junto con la fecha y hora.

---

## 🧩 Requisitos

El proyecto utiliza las siguientes librerías de Python:

- `torch` (PyTorch)
- `opencv-python`
- `matplotlib`
- `numpy`
- `easyocr`
- `pandas`
- `Pillow`

---

## 🐧 Instalación (Linux recomendada)

### 1. Clona el repositorio

	git clone https://github.com/JysusAle/placas-vehiculos.git

	cd placas-vehiculos

### 2. Crea un entorno virtual

	python3 -m venv venv

### 3. Activa el entorno virtual

	source venv/bin/activate

### 4. Instala las dependencias necesarias

	pip install -r requirements.txt

---

## ▶️ Cómo ejecutar

### En una terminal, en el directorio del proyecto ejecuta:

	python main.py

Lo que deberia hacer es detectar un numero de placa utilizando OCR de una imagen recortada, generada por
YOLOv5 y guardarla en un .csv con el nombre de `placas_detectadas.csv` 
