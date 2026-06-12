#be importáljuk a szükséges modulokat
import qrcode
import png
from pyqrcode import QRCode
#stringbe megadjuk az url-t amit qr kódá átalakitunk
url_string = "https://devdocs.io/css/reference"
#generáljuk a qr kódot a megadott url alapján
qr_code = pyqrcode.create(url_string)
#mentjük a qr kódot svg formátumban
qr_code.svg("myqr.svg", scale=8)
#mentjük a qr kódot png formátumban
qr_code.png("myqr.png", scale=6)