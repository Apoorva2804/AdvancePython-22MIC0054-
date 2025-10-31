import qrcode
data = "https://www.google.com"
qr = qrcode.make(data)
qr.save("google_qr.png")
qr.show()
print("QR Code Has Been Generated")