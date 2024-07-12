import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog, simpledialog

def create_qr_with_logo(link, logo_path, output_path):
    # Crear el QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Crear la imagen del QR code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Cargar el logo
    logo = Image.open(logo_path)

    # Calcular el tamaño del logo
    qr_width, qr_height = qr_img.size
    logo_size = qr_width // 4  # El tamaño del logo será 1/4 del tamaño del QR
    logo = logo.resize((logo_size, logo_size))

    # Calcular la posición para centrar el logo
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Pegar el logo en el QR code
    qr_img.paste(logo, pos, mask=logo)

    # Guardar la imagen final
    qr_img.save(output_path)

def main():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Solicitar el link
    link = simpledialog.askstring("Input", "Ingresa el link para el QR code:")

    if link:
        # Seleccionar el logo
        logo_path = filedialog.askopenfilename(
            title="Selecciona el logo",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )

        if logo_path:
            # Seleccionar la ruta de salida
            output_path = filedialog.asksaveasfilename(
                title="Guardar QR code",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )

            if output_path:
                create_qr_with_logo(link, logo_path, output_path)
                print("QR code creado y guardado en", output_path)
            else:
                print("No se seleccionó la ruta de salida.")
        else:
            print("No se seleccionó el logo.")
    else:
        print("No se ingresó el link.")

if __name__ == "__main__":
    main()
