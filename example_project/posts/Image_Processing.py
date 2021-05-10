import numpy as np
import cv2
import os
def order_points(pts) :
    rect = np.zeros((4,2), dtype = "float32")
    s = pts.sum(axis=1) #sum() : 넘겨받은 배열의 각 행이나 열의 합을 도출하는 함수
    rect[0] = pts[np.argmin(s)] #x+y 의 최소값
    rect[2] = pts[np.argmax(s)] #x+y 의 최대값

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)] #y-x 의 최소값
    rect[3] = pts[np.argmax(diff)] #y-x 의 최대값

    return rect

def auto_scan_image(fullPath,fname):
    image = cv2.imread(fullPath)
    orig = image.copy()
    r = 800.0 / image.shape[0]
    dim = (int(image.shape[1] * r), 800)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  # 이미지를 resize

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 이미지의 색공간을 그레이스케일로 바꿈
    gray = cv2.GaussianBlur(gray, (3, 3), 1)  # GaussianBlur를 통해 blur효과를 줌. 외곽 효과 검출 쉽게 하기 위함.
    edged = cv2.Canny(image, 170, 200)  # Canny Edge Detection 을 통해 edge 검출


    #cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    #cv2.namedWindow('Edged', cv2.WINDOW_NORMAL)
    #cv2.imshow("Image", image)
    #cv2.imshow("Edged", edged)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
    # cv2.contourArea 는 contour가 그린 면적을 의미함

    for c in cnts:
        peri = cv2.arcLength(c, True)  # contour가 그리는 길이를 반환
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        cv2.drawContours(image, [approx], -1, (0, 0, 255), 2)
        #cv2.imshow('outline', image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #cv2.waitKey(1)
        if len(approx) == 4:
            screenCnt = approx
            break

    cv2.drawContours(image, [screenCnt], -1, (255, 0, 0), 2)
    #cv2.imshow("outline", image)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.waitKey(1)

    rect = order_points(screenCnt.reshape(4, 2) / r)
    (topLeft, topRight, bottomRight, bottomLeft) = rect

    w1 = abs(bottomRight[0] - bottomLeft[0])
    w2 = abs(topRight[0] - topLeft[0])
    h1 = abs(topRight[1] - bottomRight[1])
    h2 = abs(topLeft[1] - bottomLeft[1])

    maxWidth = max([w1, w2])
    maxHeight = max([h1, h2])

    dst = np.float32([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]])

    M = cv2.getPerspectiveTransform(rect, dst)

    warped = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))

    #print("STEP 3: Apply perspective transform")
    #cv2.imshow("Warped", warped)
    result = warped.copy()
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.waitKey(1)

    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

    warped = cv2.adaptiveThreshold(warped, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)

    #cv2.imshow("Original", orig)
    #cv2.imshow("Scanned", warped)
    print('image write')
    path = fullPath.split('\orc_ori_image')
    cv2.imwrite(path[0]+'grayed_image\\'+fname, warped)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #cv2.imwrite(path[0]+'orc_ori_image\\'+fname,result)
    cv2.imwrite(path[0]+'translated_image\\'+fname,result)
    os.remove(path[0]+'orc_ori_image\\'+fname)