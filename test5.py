import cv2
import numpy as np
from matplotlib import pyplot as plt

for i in range(12, 13):
    im1 = cv2.imread('./materials/appui/0319_%d.png' % i)
    #im1 = cv2.imread('./materials/appui/0418_4.png')
    im2 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    #temp = cv2.imread('./materials/components/singleImage/play_game.png', 0)
    #temp = cv2.imread('./materials/components/base/missMatchTemplateMaterial.png', 0)
    temp = cv2.imread('./materials/components/base/sponsor_content_hk.png', 0)
    w, h = temp.shape[::-1]
    method = cv2.TM_CCOEFF_NORMED
    # method = cv2.TM_CCOEFF
    res = cv2.matchTemplate(im2, temp, method)
    threshold = 0.997
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(im1, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 12)
        print "accurately matched"


    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc

    #bottom_right = (top_left[0] + w, top_left[1] + h)
    ##
    # match_area_width = bottom_right[0] - top_left[0]
    # match_area_height = bottom_right[1] - top_left[1]
    # if (abs(float(match_area_width)/match_area_height - float(w)/h) < 0.1):
    #     print "must matched with template!"
    ##
    ###cv2.rectangle(im1, top_left, bottom_right, 255, 12)
    plt.subplot(121), plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(im1, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])


    plt.show()


    ##

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html

# def checkTemplate(img, template, method, idx, bestIdx, bestVal):
#     res = cv2.matchTemplate(img, template, method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
#     if bestVal < max_val:
#         bestVal = max_val
#         bestIdx = idx
#
#     return bestVal, bestIdx