import pyqrcode
import png
import string
import random
from PIL import Image
import qrcode



#To Create a unique String that to be placed in the QR

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))




#Creating a QR Code

def createimg():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    qr.add_data(id_generator())
    qr.make(fit=True)
    img = qr.make_image()
    img.save('QR FOR TEMPLATE'+'.jpg')


#Placing the QR in the Template Provided


def embed_qr_in_id():
    image = Image.open('template.jpg')
    logo = Image.open("qr.jpg")
    image_copy = image.copy()
    # co-ordines of the QR code Position
    position = (255, 826)
    image_copy.paste(logo, position)
    image_copy.save('IMAGE ' + str(i) + '.jpg')



i = 0

'''Main 
The Value of i is depending upon the no. of QR Code you want''' 

for i in range(1):
    createimg()
    embed_qr_in_id()
