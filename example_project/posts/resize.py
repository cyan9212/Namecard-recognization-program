import cv2

def resize(fname):

    image = cv2.imread('resource\\translated_image\\' + fname)
    resized = cv2.resize(image,(500,280),interpolation=cv2.INTER_AREA)
    cv2.imwrite('resource\\translated_image\\' + fname, resized)