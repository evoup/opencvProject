import cv2

print cv2.__version__
import numpy as np
from matplotlib import pyplot as plt

for i in range(0, 1):

    img = cv2.imread('materials/knockout/jiantu.jpg')




    # img = cv2.imread('messi5.jpg')
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (50, 50, 450, 290)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]
    plt.imshow(img), plt.colorbar(), plt.show()


    # cv2.imshow('img', edged)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
