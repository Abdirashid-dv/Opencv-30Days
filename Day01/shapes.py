import os
import cv2


img = cv2.imread(os.path.join('.','data', 'whiteboard.png'))

print(img.shape)

# Line
cv2.line(img, (100, 150), (200, 300), (0, 255, 0), 3)

# Rectangle
cv2.rectangle(img, (100, 250), (300, 450), (0, 0, 255), -1)

# Circle
cv2.circle(img, (450, 200), 75, (255, 0, 0), 10)

# Text
cv2.putText(img, 'Hey You!!', (400, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
