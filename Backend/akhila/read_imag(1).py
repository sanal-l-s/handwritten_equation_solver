import cv2

img = cv2.imread('camera_image.png')
cv2.imshow("Image", img)
cv2.waitKey(1)
