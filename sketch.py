from cv2 import imwrite
import numpy as np 
import imageio
import scipy.ndimage 
import cv2

img = "sewana.jpeg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
 # It is 2-dimensional array formula to cinvert image to gray scale
 
 
def dodge(font,back):
     final_sketch = font*255/(255-back)
     # If image is greater than 255 which i don't think is possible but still if it is there will convwet it to 255
     final_sketch[final_sketch>255]=255
     final_sketch[back==255]=255
     return final_sketch.astype("uint8")
 
 
ss = imageio.imread(img)
gray = rgb2gray(ss)
 
i = 255-gray
 
 
blur = scipy.ndimage.filters.gaussian_filter(i,sigma =15)
 
r=dodge(blur,gray)
 
cv2,imwrite("sewana.png",r)