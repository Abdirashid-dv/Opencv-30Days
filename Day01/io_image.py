import cv2
import os

# Read Image
img = cv2.imread('data/bear.png')

'''
# type is numpy.ndarray
print(type(img))

# shape is tuple that contain (height, weight, channel (RGB))
print(img.shape)
'''

# Write Image
cv2.imwrite('out_bird.png', img)

# Visualize Image
cv2.imshow('image', img)
cv2.waitKey(0)

