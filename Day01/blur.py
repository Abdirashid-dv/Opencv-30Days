import cv2
import os


img = cv2.imread(os.path.join('.', 'data', 'fizikci.png'))
resized_img = cv2.resize(img, (350, 455))

k_size = 11
img_blur = cv2.blur(resized_img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(resized_img, (k_size, k_size), 3)
img_median = cv2.medianBlur(resized_img, k_size)

cv2.imshow('img', resized_img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median', img_median)

cv2.waitKey(0)
