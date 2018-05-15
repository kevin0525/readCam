import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('My Camera',frame)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()
