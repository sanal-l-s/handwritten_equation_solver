import numpy as np
import cv2

img1 = cv2.imread('49.png')
cv2.imshow("binary image",img1)
print("size=",img1.shape)
s=img1.shape
r=s[0]
c=s[1]
print("number of rows",r)
print("numbder of columns",c)

red=np.zeros((r,c,1),dtype="uint8")
green=np.zeros((r,c,1),dtype="uint8")
blue=np.zeros((r,c,1),dtype="uint8")

for i in range(r):
    for j in range(c):
        red[i,j]=img1[i,j,0]
        green[i,j]=img1[i,j,1]
        blue[i,j]=img1[i,j,2]
cv2.imshow("Red",red)
cv2.imshow("green",green)
cv2.imshow("blue",blue)
# convert to black and white

bw_image =np.zeros((r,c,1))
thresh=80
for i in range(r):
    for j in range(c):
        if(red[i,j]>thresh):
            bw_image[i,j]=1

cv2.imshow("bwimage",bw_image)
cv2.waitKey()
