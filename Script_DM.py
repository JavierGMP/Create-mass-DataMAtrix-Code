#pip install pylibdmtx
#pip install pillow


from pylibdmtx.pylibdmtx import encode
from pylibdmtx.pylibdmtx import decode
from PIL import Image, ImageFont, ImageDraw 
import os
import cv2
import time


location_string = "B."
directory = os.getcwd()

for i in range(6):
    
    zero_fill = str(i).zfill(3)
    iterate_string = location_string + str(i)
    

    encoded = encode(iterate_string.encode('utf8'))#, scheme="Ascii", size = "32x32")
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    
    barcode="B.{}.png".format(zero_fill)
    dbarcode = directory +"\\"+barcode
    
    img.save(dbarcode)
    
    print(decode(Image.open(dbarcode)))
    
time.sleep(2)

for j in range(6):
    
    zero_fill=str(j).zfill(3)
    barcode="\\B.{}.png".format(zero_fill)
    title="B.{}".format(zero_fill)
    dire = os.getcwd() + barcode
    org = (180,470)
    font = cv2.FONT_HERSHEY_PLAIN
    fontScale = 3
    color = (3, 0, 0)
    thickness = 2
    direc = os.getcwd() + barcode
    
    
    
    image=cv2.imread(dire)

    scale_percent=7
    width=int(image.shape[1]*scale_percent)
    height=int(image.shape[0]*scale_percent)
    dimension=(width,height)
    resized = cv2.resize(image,dimension, interpolation = cv2.INTER_AREA)

    print(resized.shape)
    
    cv2.putText(resized, title, org, font, fontScale, color, thickness, cv2.LINE_AA)
    
    cv2.imwrite("ResB.{}.png".format(zero_fill),resized)
    os.remove(direc)
