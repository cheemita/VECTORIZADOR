import cv2
from PIL import Image
import numpy as np
from tkinter import Tk, filedialog
import subprocess
import os

def vectorize_image(input_path, output_path):
    # Cargar la imagen en escala de grises
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    
    # Convertir la imagen a blanco y negro
    _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    
    # Guardar la imagen binaria temporalmente
    temp_path = "temp_image.png"
    cv2.imwrite(temp_path, binary_img)
    
    # Usar Inkscape para vectorizar la imagen
    subprocess.run([
        "inkscape",
        temp_path,
        "--export-type=svg",
        "--export-filename=" + output_path
    ])
    
    # Eliminar el archivo temporal
    os.remove(temp_path)
    
    print("Vectorization complete! Check the output file.")

# Inicializar la ventana de Tkinter
root = Tk()
root.withdraw()  # Ocultar la ventana principal

# Abrir cuadro de diálogo para seleccionar archivo
input_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
)

# Verificar si se seleccionó un archivo
if input_path:
    output_path = filedialog.asksaveasfilename(
        title="Save SVG As",
        defaultextension=".svg",
        filetypes=[("SVG files", "*.svg")]
    )
    
    # Ejecutar la vectorización si se seleccionó una ruta de salida
    if output_path:
        vectorize_image(input_path, output_path)
else:
    print("No file selected.")
