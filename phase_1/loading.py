import cv2

image = cv2.imread("media/images.jpeg")

if image is None:
    print("Image Not Found")
else:
    print("Loaded Successfully")
    cv2.imshow("Images",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

