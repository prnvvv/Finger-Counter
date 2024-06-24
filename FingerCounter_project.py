import cv2  # OpenCV library for computer vision tasks
import time  # Time library to calculate frame rate
import HandTrackerModule as htm  # Custom module for hand tracking

# Initialize video capture object to read from webcam
capture = cv2.VideoCapture(0)
# Set the width of the video frame
capture.set(3, 640)
# Set the height of the video frame
capture.set(4, 480)

# Check if the webcam is opened successfully
if not capture.isOpened():
    raise Exception("Error: Loading not successful.")

# Variable to store the previous time for FPS calculation
previousTime = 0

# Initialize the hand detector with minimum detection and tracking confidence
detector = htm.HandDetector(min_detection_confidence=0.75, min_tracking_confidence=0.75)

# List of tip IDs for each finger (thumb, index, middle, ring, pinky)
tipID = [4, 8, 12, 16, 20]

while True:
    # Read frame from webcam
    success, vidObject = capture.read()
    if not success:
        raise Exception("Error: Reading frame was not successful.")
    
    # Detect hands in the frame
    vidObject = detector.detectHands(vidObject)
    # Find positions of hand landmarks
    lmList = detector.findPosition(vidObject, draw=False)
    
    if len(lmList) != 0:
        fingers = []
        # Check for each finger if it is up or down
        for id in range(4):
            if lmList[tipID[id]][2] < lmList[tipID[id] - 2][2]:
                fingers.append(1)  # Finger is up
            else:
                fingers.append(0)  # Finger is down
    
        count = fingers.count(1)  # Count the number of fingers that are up
        print(count)  # Print the count
    
    # Calculate FPS
    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
    
    # Display the frame with the hand landmarks
    cv2.imshow("Webcamera", vidObject)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Break the loop if 'q' is pressed

# Release the webcam and close all OpenCV windows
capture.release()
cv2.destroyAllWindows()
