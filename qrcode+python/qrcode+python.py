#pip install qrcode Image

import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,

    )

img_url = "https://www.instagram.com/notypehee/"
qr_gen = qrcode.make(img_url)
qr_gen.save("notypehee.png")
