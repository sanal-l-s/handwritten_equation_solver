import cv2

cam = cv2.VideoCapture(0)

while True:
    a, img = cam.read()
    
    cv2.putText(img, "Place face In the box",(50,70),cv2.FONT_HERSHEY_DUPLEX,2,(120,120,0),2)
    cv2.rectangle(img, (180,180), (400,400), (20,20,20), 2)
    cv2.imshow("Image Frame", img)

    key = cv2.waitKey(1)

    if(key == ord('q')):
       break
    if(key == ord('c')):

       cv2.imwrite("img_capture.png",img)
       break

cam.release()
cv2.destroyAllWindows()
