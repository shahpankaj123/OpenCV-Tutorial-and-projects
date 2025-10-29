import cv2 as cv

image = cv.imread("media/images.jpeg")

if image is not None:
    cv.imwrite("media/save_img.jpeg",image)
    print("image save successfully....")
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imwrite('media/save_img_gray.jpeg', gray)

