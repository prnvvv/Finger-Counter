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
        ThumbFingerup = (lmList[[4][2] < lmList[3][2]])
        IndexFingerup = (lmList[8][2] < lmList[6][2])
        MiddleFingerup = (lmList[12][2] < lmList[10][2])
        RingFingerup = (lmList[16][2] < lmList[14][2])
        PinkyFingerup = (lmList[20][2] < lmList[18][2])

    currenTime = time.time()
    fps = 1 / (currenTime - previousTime)
    previousTime = currenTime

    cv2.imshow("Webcamera", vidObject)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
