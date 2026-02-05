import qrcode

# Google Drive link of my Python completion certificate as data
data = "https://drive.google.com/file/d/1mljxh4qnL64aqsMlKKph1soxm3WWoUn3/view?usp=drivesdk"

# Creating QR code
qr = qrcode.make(data)

# Saving QR code as image
qr.save("my_qr_code.png")

print("QR Code generated successfully ✅")
