import cv2
import time

capture = cv2.VideoCapture(0)

capture.set(3, 640)
capture.set(4, 480)

if not capture.isOpened():
    raise Exception("Error: Loading not successful.")

previousTime = currenTime = 0

while True:
    success, vidObject = capture.read()

    if not success:
        raise Exception("Error: Reading frame was not successful.")

    currenTime = time.time()
    fps = 1 / (currenTime - previousTime)
    previousTime = currenTime
    
    cv2.imshow("Webcamera", vidObject)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
