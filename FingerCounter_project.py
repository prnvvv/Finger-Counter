import cv2
import time
import HandTrackerModule as htm

capture = cv2.VideoCapture(0)

capture.set(3, 640)
capture.set(4, 480)

if not capture.isOpened():
    raise Exception("Error: Loading not successful.")

previousTime = currenTime = 0

detector = htm.HandDetector(min_detection_confidence = 0.75, min_tracking_confidence = 0.75)

tipID = [4, 8, 12, 16, 20]

while True:
    success, vidObject = capture.read()

    if not success:
        raise Exception("Error: Reading frame was not successful.")

    vidObject = detector.detectHands(vidObject)

    lmList = detector.findPosition(vidObject, draw = False)
    
    if len(lmList) != 0:
        fingers = []
        for id in range(0, 5):
            if (lmList[tipID[id]][2] < lmList[tipID[id] - 2][2]):
                fingers.append(1)
            else:
                fingers.append(0)
        
        print(fingers.count(1))

    currenTime = time.time()
    fps = 1 / (currenTime - previousTime)
    previousTime = currenTime

    cv2.imshow("Webcamera", vidObject)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
