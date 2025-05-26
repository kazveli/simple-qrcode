from PIL import Image
import qrcode

#Cria o objeto
qr = qrcode.QRCode(version=10, box_size=10, border=2)

#Define os dados do qrcode
data = "https://www.example.com/"
qr.add_data(data)

#Monta o qrcode
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

#Logotipo
logo = Image.open("logotipo.png")
logo = logo.resize((125,125))
img_w, img_h = img.size 
logo_w, logo_h = logo.size 
pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
img.paste(logo,pos)

#Salve o qrcode
img.save("qr-code.png")