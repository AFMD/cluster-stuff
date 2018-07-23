import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=1,
    border=4,
)

data = "99999999999999999"
data = qrcode.util.QRData(data, mode=qrcode.util.MODE_NUMBER, check_data=False)

qr.add_data(data, optimize=0)

qr.make(fit=False)
qr.print_ascii(tty=False, invert=False)

print(qr.box_size)
print(qr.version)

img = qr.make_image(fill_color="black", back_color="white")

f = open('/tmp/qr2.png', 'wb')
img.save(f)
f.close()
