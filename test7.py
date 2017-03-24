import cv2
from matplotlib import pyplot as plt

img = cv2.imread('materials/turtials/gradient.jpg', 0)
_, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
__, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
___, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
____, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_____, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
