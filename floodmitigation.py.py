import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image 


#Crop the black and withe segmented output image to work on it
#Crop Dimensions : 
left = 350
top  = 150
right = 575
bottom =355

imgcrop = Image.open('flood1output.png')
img2_crop = imgcrop.crop((left, top, right, bottom))
plt.imshow(img2_crop)
img2_crop.save('flood1crop_output.png')

#Read the image 

img3_gray = cv2.imread('flood1crop_output.png',0)
plt.imshow(img3_gray,cmap='gray')
print('gray scale image shape : ',img3_gray.shape)

white = np.sum(img3_gray != 0)
print('number of white pixels : ',white)

black = np.sum(img3_gray == 0)
print('number of white pixels : ',black)

print('total number of pixels: ',img3_gray.size)


Percentage_green = (black/img3_gray.size)*100
Percentage_water = (white/img3_gray.size)*100
print("Percentage of tree cover in the image is : ",Percentage_green,"%")
print("Percentage of water in the image is : ",Percentage_water,"%")

