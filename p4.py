import cv2
img = cv2.imread('1.png')
#cv2.imshow("Image2", img)
imgsize=img.shape

print("size mof colour image=",imgsize)

gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray_image)
imgsize1=gray_image.shape
cv2.imwrite("imgg.png",gray_image)
print("grayimage size=",imgsize1)

a=len(imgsize1)

#if(a==3):
 #   print("color image")
#elif(a==2):
  #        print("gray image")
(thresh,binary)=cv2.threshold(gray_image,100,255,cv2.THRESH_BINARY)
print(thresh)
cv2.imshow("binary",binary)
print(binary.shape)
cv2.imwrite("imgb.png",binary)
cv2.waitKey()
