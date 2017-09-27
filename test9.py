import cv2

print cv2.__version__
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('materials/appui/0319_12.jpg',0)
# height, width = img.shape[:2]
# img = cv2.resize(img,(402, 743), interpolation = cv2.INTER_LINEAR)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# laplacian = cv2.Laplacian(img,cv2.CV_64F)
# sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
# plt.show()

# img = cv2.imread('materials/appui/0319_14.jpg', 0)
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
for i in range(0, 1):
    # for i in range(12, 13):
    img = cv2.imread('materials/knockout/jiantu.jpg')
    height, width = img.shape[:2]
    img = cv2.resize(img, (402, 743), interpolation=cv2.INTER_LINEAR)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgray = cv2.bilateralFilter(imgray, 11, 17, 17)
    edged = cv2.Canny(imgray, 30, 200)
    ####
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # l_b = np.array([110, 50, 50])
    # h_b = np.array([130, 255, 255])
    # mask = cv2.inRange(hsv, l_b, h_b)
    # res = cv2.bitwise_and(img, img, mask=mask)
    ####
    # ret, thresh = cv2.threshold(imgray, 250, 255, 0)
    # image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # #######
    # for cnt in contours:
    #     x, y, w, h = cv2.boundingRect(cnt)
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #     rect = cv2.minAreaRect(cnt)
    #     box = cv2.boxPoints(rect)
    #     box = np.int0(box)
    #     cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
        #######
        # find biggest contour, may be material
    # img = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    # img = cv2.drawContours(imgray, contours, 3, (0, 0, 255), 3)
    cv2.imshow('img', edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
