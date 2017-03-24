import cv2
print cv2.__version__
import numpy as np
#from matplotlib import pyplot as plt
img = cv2.imread('materials/appui/0319_12.jpg',1)
height, width = img.shape[:2]
img = cv2.resize(img,(402, 743), interpolation = cv2.INTER_LINEAR)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
