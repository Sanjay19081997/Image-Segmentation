import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image 

left = 350
top  = 150
right = 575
bottom =355

imgcrop = Image.open('flood2output.png')
img2_crop = imgcrop.crop((left, top, right, bottom))
plt.imshow(img2_crop)
img2_crop.save('flood2crop_output.png')
img3_gray = cv2.imread('flood2crop_output.png',0)
plt.imshow(img3_gray,cmap='gray')
img3_gray.shape

lefta = 0
topa  = 0
righta = 225
bottoma = 120
img2_cropa = img2_crop.crop((lefta, topa, righta, bottoma))
plt.imshow(img2_cropa)
img2_cropa.save('flood2cropa.png')
img3_graya = cv2.imread('flood2cropa.png',0)
plt.imshow(img3_graya,cmap='gray')
print('shape of image flood2cropa: ', img3_graya.shape)
blacka = np.sum(img3_graya == 0)
whitea = np.sum(img3_graya == 255)
graya =  (120*225) - (whitea+blacka)
Percentage_green_a = (blacka/img3_graya.size)*100
Percentage_water_a = (whitea/img3_graya.size)*100
Percentage_land_a = (graya/img3_graya.size)*100
print("Percentage of tree cover in the image flood2cropa is : ",Percentage_green_a,"%")
print("Percentage of water in the image flood2cropa is : ",Percentage_water_a,"%")
print("Percentage of land and building in the image flood2cropa is : ",Percentage_land_a,"%")


leftb = 0
topb  = 121
rightb = 225
bottomb = 205
img2_cropb = img2_crop.crop((leftb, topb, rightb, bottomb))
plt.imshow(img2_cropb)
img2_cropb.save('flood2cropb.png')
img3_grayb = cv2.imread('flood2cropb.png',0)
plt.imshow(img3_grayb,cmap='gray')
print('shape of image flood2cropb: ',img3_grayb.shape)
blackb = np.sum(img3_grayb == 0)
whiteb = np.sum(img3_grayb == 255)
grayb =  (84*225) - (whiteb+blackb)
Percentage_green_b = (grayb/img3_grayb.size)*100
Percentage_water_b = ((whiteb+blackb)/img3_grayb.size)*100
print("Percentage of tree cover in the image flood2cropb is : ",Percentage_green_b,"%")
print("Percentage of water in the image flood2cropb is : ",Percentage_water_b,"%")

Percentage_green_total = ((blacka+grayb)/(img3_graya.size+img3_grayb.size))*100
Percentage_water_total = ((whiteb+blackb+whitea)/(img3_graya.size+img3_grayb.size))*100
Percentage_land_total = (graya/(img3_graya.size+img3_grayb.size)*100)
print("Percentage of tree cover in the image flood2crop is : ",Percentage_green_total,"%")
print("Percentage of water in the image flood2crop is : ",Percentage_water_total,"%")
print("Percentage of land and building in the image flood2crop is : ",Percentage_land_total,"%")