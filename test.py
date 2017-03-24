import cv2

print cv2.__version__
import numpy as np

# from matplotlib import pyplot as plt
#img = cv2.imread('materials/appui/0319_12.png', 1)
im_gray = cv2.imread('materials/appui/0319_12.png', 0)
height, width = im_gray.shape[:2]
img = cv2.resize(im_gray, (402, 743), interpolation=cv2.INTER_LINEAR)

# thresh = 127
# im_bw = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
