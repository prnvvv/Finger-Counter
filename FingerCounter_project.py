import cv2
import time
import HandTrackerModule as htm

capture = cv2.VideoCapture(0)

capture.set(3, 640)
capture.set(4, 480)

if not capture.isOpened():
    raise Exception("Error: Loading not successful.")

previousTime = currenTime = 0

detector = htm.HandDetector()

while True:
    success, vidObject = capture.read()

    if not success:
        raise Exception("Error: Reading frame was not successful.")

    vidObject = detector.detectHands(vidObject)

    lmList = detector.findPosition(vidObject, draw = False)
    
    if len(lmList) != 0:
        if lmList[8][2] < lmList[6][2]:
            print("Index finger is up")

    currenTime = time.time()
    fps = 1 / (currenTime - previousTime)
    previousTime = currenTime

    cv2.imshow("Webcamera", vidObject)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
