import cv2 as cv

def rescale(frame , size = 0.7):
    height = int(frame.shape[0] * size)
    width = int(frame.shape[1] * size)

    dimensions = (width , height)

    return cv.resize(frame ,dimensions ,interpolation=cv.INTER_AREA) 

cap = cv.VideoCapture(0)
while 1:
    st ,frame = cap.read()

    cv.imshow('frame' , rescale(frame))
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


