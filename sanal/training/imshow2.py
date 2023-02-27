import cv2

img = cv2.imread('image1.png')
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#cv2.imshow("Image", img)
#cv2.imshow("Image Gray", gray_image)

#show image size


imgsize = img.shape
print("Color image size",imgsize)

gray_imgsize = gray_image.shape
print("Gray Image Size",gray_imgsize)


print("Number of rows = ",imgsize[0])
print("Number of columns = ",imgsize[1])
print(imgsize[2])

#print length of tuple
print("Length of color image tuple",len(imgsize))
print("Length of gray image tuple",len(gray_imgsize))

color_img_size = len(imgsize)
gray_image_size = len(gray_imgsize)

if(gray_image_size==3):
    print("Colour Image")
elif (gray_image_size==2):
    print("Gray Image")
    

cv2.waitKey()
