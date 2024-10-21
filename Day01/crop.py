import cv2
import os

img = cv2.imread(os.path.join('.', 'bear.png'))

'''Indexka kowaad waa Height, ka Labaad Width '''
cropped_img = img[160:600, 620:1180]
print(img.shape)

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
