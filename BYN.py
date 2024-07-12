import cv2
from tkinter import Tk, filedialog

def optimize_for_laser_engraving(input_path, output_path):
    # Cargar la imagen en color
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)
    
    # Aplicar filtro bilateral para suavizar la imagen mientras se conservan los bordes
    smoothed_img = cv2.bilateralFilter(img, 9, 75, 75)
    
    # Convertir la imagen a escala de grises
    gray_img = cv2.cvtColor(smoothed_img, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbral adaptativo para obtener una imagen binaria
    binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    
    # Guardar la imagen optimizada para grabación láser
    cv2.imwrite(output_path, binary_img)
    
    print(f"Laser-optimized image saved to {output_path}")

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
        title="Save Laser-optimized Image As",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("Bitmap files", "*.bmp")]
    )
    
    # Ejecutar la optimización si se seleccionó una ruta de salida
    if output_path:
        optimize_for_laser_engraving(input_path, output_path)
else:
    print("No file selected.")
