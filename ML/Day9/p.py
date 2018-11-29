import cv2 as cv
import numpy as np
img=cv.imread('walking.jpg',0)
print(img.shape)
print(img)

img1=img
img1[0:100,0:100]=np.zeros((100,100))
cv.imwrite('n.jpg',img1)


img2=cv.imread('n.jpg',0)

i=np.subtract(img,img1)
print(i)

print(img)
cv.imshow('image',i)
k=cv.waitKey(0)

