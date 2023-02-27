import cv2
import time

cam = cv2.VideoCapture(0)

while True:
    a, img = cam.read()
    #print(a)
    cv2.imshow("Image Frame", img)

    key = cv2.waitKey(1)

    if(key == ord('q')):
       break
    if(key == ord('c')):

       cv2.imwrite("image1.png",img)
       break

cam.release()
cv2.destroyAllWindows()

time.sleep(1)

imgres = cv2.imread('image1.png')
cv2.imshow("Image",imgres)
cv2.waitKey()


