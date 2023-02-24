#addv string to image
import cv2
img=cv2.imread("33.png")
cv2.putText(img,"hello",(80,100),cv2.FONT_HERSHEY_DUPLEX,3,(255,0,255),4)
cv2.rectangle(img,(5,5),(100,50),(0,0,250),3)#lefttopcorner,right bottom corner,colour,thickness
cv2.imshow("image33",img)
cv2.waitKey(0)
