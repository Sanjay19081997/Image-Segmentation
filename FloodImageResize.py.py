import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image 

img = cv2.imread('floodorg.jpg')
type(img)
img.shape
fix_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
new_image = cv2.resize(fix_img,(40,40))
plt.imshow(new_image)
cv2.imwrite('flood1.jpg',new_image)


