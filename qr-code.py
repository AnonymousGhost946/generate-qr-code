from qrcode import QRCode

qr= QRCode(version=1,box_size=10,border=5)

data="https://github.com/AnonymousGhost946?tab=repositories"#you can replace with your link of website or watsapp or else

qr.add_data(data)

qr.make(fit=True)

img=qr.make_image(fill_color="black",back_color="white")

img.save("qr_code.png")

