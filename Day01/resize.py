import cv2
import os

img = cv2.imread(os.path.join('.', 'bear.png'))
resized_img = cv2.resize(img, (640, 426))

print(img.shape)
print(resized_img.shape)

cv2.imshow('image', img)
cv2.imshow('resized_img', resized_img)

cv2.waitKey(0)
