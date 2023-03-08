import cv2

img = cv2.imread('image1.png')
cv2.imshow("Image", img)

#show image size
imgsize = img.shape
print(imgsize)

cv2.waitKey()
