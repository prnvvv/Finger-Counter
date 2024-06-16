import cv2

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    raise Exception("Error: Loading not successful.")

while True:
    success, vidObject = capture.read()

    if not success:
        raise Exception("Error: Reading frame was not successful.")

    cv2.imshow("Webcamera", vidObject)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
