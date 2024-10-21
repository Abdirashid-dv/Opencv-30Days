import cv2

# Read Video
video_path = (r'C:\Users\Abdirashid\Videos\Captures\abdirashid_dv@LAPTOP-TQKI2E7F_ ~_100Days-of-code-python_Day-07 '
              r'2023-03-24 18-52-13.mp4')

video = cv2.VideoCapture(video_path)

# Visualize Video

ret = True

while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()
