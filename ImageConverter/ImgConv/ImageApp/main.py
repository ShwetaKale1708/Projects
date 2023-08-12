import cv2
import os
import numpy as np
from PIL import  Image,ImageFilter
def pp(img="",choice=""):
    kk=str(os.getcwd())+"/media"
    print("img",img,'kk',kk)
    kk=os.path.join(kk,str(img))
    
    if choice=="I2S":
        img=I2S(kk)
    elif choice=="I2B":
        img=I2B(kk)
    elif choice=="I2BW":
        img=I2BnW(kk)
    elif choice=="I2C":
        img=I2C(kk)
    if "media" in img:
        a=(img.index('media'))+6
        img=img[a::]
  
    return img

def I2C(img):
    
    image = cv2.imread(img)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color = cv2.bilateralFilter(image,9,250,250)
    cartoon = cv2.bitwise_and(color,color,mask=edges)

    if '.jpg' in img:
        img=img.replace(".jpg",'I2C.jpg')
    elif '.jpeg' in img:
        img=img.replace(".jpeg",'I2C.jpeg')
    elif '.png' in img:
        img=img.replace(".png",'I2C.png')

    cv2.imwrite(img,cartoon)
    return img
def I2S(img):
    image=cv2.imread(img)
    grey_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    invert_img=cv2.bitwise_not(grey_img)
    blur=cv2.GaussianBlur(invert_img,(21,21),0)
    invertedblur=cv2.bitwise_not(blur)
    sketch=cv2.divide(grey_img,invertedblur,scale=256.0)
    img=str(img)
    if '.jpg' in img:
        img=img.replace(".jpg",'I2S.jpg')
    elif '.jpeg' in img:
        img=img.replace(".jpeg",'I2S.jpeg')
    elif '.png' in img:
        img=img.replace(".png",'I2S.png')

    cv2.imwrite(img,sketch)
    return img
    
def I2BnW(img): 
    image=Image.open(img)
    bw_image=image.convert('L')
    if '.jpg' in img:
        img=img.replace(".jpg",'I2BnW.jpg')
    elif '.jpeg' in img:
        img=img.replace(".jpeg",'I2BnW.jpeg')
    elif '.png' in img:
        img=img.replace(".png",'I2BnW.png')
    bw_image.save(img)
    return img
def I2B(img):
    image=Image.open(img)
    blur=image.filter(ImageFilter.GaussianBlur(9))
    if '.jpg' in img:
        img=img.replace(".jpg",'I2B.jpg')
    elif '.jpeg' in img:
        img=img.replace(".jpeg",'I2B.jpeg')
    elif '.png' in img:
        img=img.replace(".png",'I2B.png')
    blur.save(img)
    return img
    
