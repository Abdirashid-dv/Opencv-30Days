import os

import cv2

img = cv2.imread(os.path.join('.', 'data', 'bear.png'))

# resized
resized_img = cv2.resize(img, (720, 405))

# color to gray
img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# img_gray to threshold
res, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

# thresh = cv2.blur(thresh, (10, 10))
#
# res, thresh = cv2.threshold(thresh, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('resized_img', resized_img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
