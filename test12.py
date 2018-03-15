import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv.imread('./materials/others/mario.png')
# img_rgb = cv.imread('./materials/appui/0319_12.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('./materials/others/coin.png',0)
# template = cv.imread('./materials/components/base/sponsor_content_hk2.png',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res_mario.png',img_rgb)