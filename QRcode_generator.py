import qrcode as qr

link = input("Enter the Link or Text you want to make the QR CODE -->>\n")
img = qr.make(link)

f_name = input("Image name you want to save it ( along with format name !) \n")
img.save(f_name)

# To change it's color !

from PIL import Image 

qr = 