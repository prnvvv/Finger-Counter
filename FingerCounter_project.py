import HandTrackerModule as htm
import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    raise Exception("Error: Loading not succcessful.")

while True:
    success, vidObject = capture.read()

    if not success:
        raise Exception("Error: Loading not succcessful.")
    
    cv2.imshow("Webcamera", vidObject)

capture.release()
cv2.destroyAllWindows()