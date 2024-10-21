import cv2
import os

img = cv2.imread(os.path.join('.', 'bird.png'))
img_resized = cv2.resize(img, (350, 455))

img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img_resized, cv2.COLOR_BGR2HSV)

# cv2.imshow('img', img)
cv2.imshow("img_resized", img_resized)
# cv2.imshow('img_rgb', img_rgb)
# cv2.imshow('img_gray', img_gray)
cv2.imshow('img_hsv', img_hsv)

cv2.waitKey(0)
