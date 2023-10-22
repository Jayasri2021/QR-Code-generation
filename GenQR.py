import qrcode
import tkinter as tk
from PIL import Image, ImageTk


# Function to generate a QR code
def generate_qr_code():
    text = entry.get()  # Get text from the input field
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=7,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("generated_qr.png")  # Save the QR code as an image
    # Display the QR code image above the input field
    qr_image = Image.open("generated_qr.png")
    qr_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image


# Create the main window
window = tk.Tk()
window.title("QR Code Generator -'StudyMuch'")

# Create an input field for the user to enter text
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Create a button to generate the QR code
generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create a label to display the QR code image
qr_label = tk.Label(window)
qr_label.pack()
# Start the main loop
window.mainloop()
