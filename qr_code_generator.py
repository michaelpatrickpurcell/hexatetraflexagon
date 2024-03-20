# scaled_qrcode.py

import segno

qrcode = segno.make_qr("https://armigergames.itch.io/missing-monsters")
qrcode.save(
    "scaled_qrcode.png",
    scale=1.0,
    light="#faf9a5",
)

