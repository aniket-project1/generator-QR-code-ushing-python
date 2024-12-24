
import qrcode

# Data you want to encode
data = "https://www.linkedin.com/in/aniket-kalushe-92005431a/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the image to a file
img.save("example_qr_code.png")

# Optionally, show the image
img.show()
