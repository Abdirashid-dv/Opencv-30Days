import cv2


# Read WebCam
''':parameter waxa la gelinayaa ID'ga Camerada'''
webcam = cv2.VideoCapture(0)

# Visualize Webcam
while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
