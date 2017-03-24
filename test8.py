import cv2
print cv2.__version__

# from matplotlib import pyplot as plt
im_gray = cv2.imread('materials/appui/0319_14.png', 0)
height, width = im_gray.shape[:2]
img = cv2.resize(im_gray, (402, 743), interpolation=cv2.INTER_LINEAR)

_, img = cv2.threshold(img, 254, 255, cv2.THRESH_BINARY)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
