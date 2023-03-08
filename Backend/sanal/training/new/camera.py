import cv2

cam = cv2.VideoCapture(0)

count=0
while True:

    a, img = cam.read()
    
    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    print(key)
    if(key == ord('q')):
        
        imgname=str(count)+".png"
       

        cv2.imwrite(imgname,img)
        count=count+1
        print ("capturing")
     

cam.release()
cv2.destroyAllWindows()
