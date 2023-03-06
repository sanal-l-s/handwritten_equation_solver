import cv2

# Load Image
img = cv2.imread("49.png")

# Prepare crop area
width, height = 700, 550
x, y = 200, 50

# Crop image to specified area using slicing
crop_img = img[y:y+height, x:x+width]

# Show image
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
