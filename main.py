from PIL import Image
import qrcode, sys

#Cria o objeto
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

#Define os dados do qrcode
data = " ".join(sys.argv[1:])
qr.add_data(data)

#Monta o qrcode
qr.make(fit=True)

#Logotipo
logo = Image.open("logotype.png")
logo = logo.convert("RGB")
base_width = qr.modules_count * 5
logo = logo.resize((int(base_width / 3), int(base_width /3)))

logo_w, logo_h = logo.size 
img = qr.make_image().convert("RGB")
img_w, img_h = img.size
offset_x = (img_w - logo_w) // 2
offset_y = (img_h - logo_h) // 2
img.paste(logo, (offset_x, offset_y))

#Salve o qrcode
img.show()