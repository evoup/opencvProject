import cv2
import numpy as np
from matplotlib import pyplot as plt

for i in range(12, 13):
    im1 = cv2.imread('./materials/appui/0319_%d.png' % i)
    im2 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    #temp = cv2.imread('./materials/test/singleImage/play_game.png', 0)
    temp = cv2.imread('./materials/test/base/sponsor_content.png', 0)
    w, h = temp.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED
    # method = cv2.TM_CCOEFF
    res = cv2.matchTemplate(im2, temp, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(im1, top_left, bottom_right, 255, 12)
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(im1, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])


    plt.show()


    ##

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
