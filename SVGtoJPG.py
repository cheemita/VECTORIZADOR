import cairosvg
from PIL import Image
import io
import tkinter as tk
from tkinter import filedialog

def svg_to_jpg(input_path, output_path, width=None, height=None, quality=85):
    # Convertir SVG a PNG en memoria
    png_data = cairosvg.svg2png(url=input_path, output_width=width, output_height=height)
    
    # Abrir la imagen PNG desde la memoria
    image = Image.open(io.BytesIO(png_data))
    
    # Convertir PNG a JPG
    rgb_image = image.convert('RGB')
    
    # Guardar la imagen JPG
    rgb_image.save(output_path, format='JPEG', quality=quality)
    print(f'Converted {input_path} to {output_path}')

def select_file_and_convert():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    file_path = filedialog.askopenfilename(
        title="Select SVG File",
        filetypes=[("SVG Files", "*.svg")]
    )
    if file_path:
        output_path = filedialog.asksaveasfilename(
            title="Save JPG File",
            defaultextension=".jpg",
            filetypes=[("JPG Files", "*.jpg")]
        )
        if output_path:
            svg_to_jpg(file_path, output_path, width=800, height=600)

if __name__ == "__main__":
    select_file_and_convert()
