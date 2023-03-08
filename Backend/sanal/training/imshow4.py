#show text on picture
import cv2

img = cv2.imread('image1.png')

cv2.putText(img, "Python",(50,70),cv2.FONT_HERSHEY_DUPLEX,2,(120,120,0),5)
cv2.rectangle(img, (100,100), (200,50), (20,0,150), 3)
cv2.imshow("Image",img)

cv2.waitKey()





#TASK
#live camera
#Show rectangle and title
# prompt to show face on rdctangle

#capture
