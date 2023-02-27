import cv2

img1 = cv2.imread('3.png')
cv2.imshow("Image1", img1)

gray_image=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image",gray_image)

imgsize1=img1.shape
print(imgsize1)

imgsize2=gray_image.shape
print(imgsize2)

print(len(imgsize1))
print(len(imgsize2))
a=len(imgsize1)
b=len(imgsize2)


if(a==3):
    print("image1 color image")
if(b==2):
    print("image2 gray scale image")
