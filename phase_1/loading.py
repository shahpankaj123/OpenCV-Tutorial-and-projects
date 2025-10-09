import cv2

image = cv2.imread("media/images.jpeg")

if image is None:
    print("Image Not Found")
else:
    print("Loaded Successfully")

