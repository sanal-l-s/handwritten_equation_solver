#show text on picture
import cv2

img = cv2.imread('image1.png')

cv2.putText(img, "Python",(50,70),cv2.FONT_HERSHEY_DUPLEX,0.6,(120,120,0),2)
cv2.imshow("Image",img)

cv2.waitKey()
