import numpy as np
import cv2

img = cv2.imread('image1.png')
cv2.imshow("Image",img)
s=img.shape
print("size=",s)
R=s[0]
C=s[1]
print("number of rows",R)
print("numbder of columns",C)


#separate Red Green Blue
red=np.zeros((R,C,1), dtype="uint8") #8 bit; 0-255
green=np.zeros((R,C,1), dtype="uint8")
blue=np.zeros((R,C,1), dtype="uint8")

for i in range (R):
    for j in range (C):
        red[i,j] = img[i,j,0]
        green[i,j] = img[i,j,1]
        blue[i,j] = img[i,j,2]


cv2.imshow("Red",red)
cv2.imshow("Green",green)
cv2.imshow("Blue",blue)


##convert to black and white
bw_image = np.zeros((R,C,1))
thresh = 80

for i in range (R):
    for j in range (C):
        if(red[i,j]>thresh):
            bw_image[i,j] = 1
cv2.imshow("BW Image",bw_image)






cv2.waitKey()
