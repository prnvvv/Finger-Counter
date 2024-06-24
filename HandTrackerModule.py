import cv2  # OpenCV library for computer vision tasks
import mediapipe as mp  # MediaPipe library for hand tracking
import time  # Time library to calculate frame rate

# HandDetector class for detecting hands and finding hand landmarks
class HandDetector:
    def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        # Initialize MediaPipe hands solution
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=static_image_mode,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        # Initialize MediaPipe drawing utility
        self.mpDraw = mp.solutions.drawing_utils

    def detectHands(self, img, draw=True):
        # Convert the frame to RGB as MediaPipe uses RGB format
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Process the frame to detect hands
        self.results = self.hands.process(imgRGB)

        # Draw hand landmarks if hands are detected
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        # Extract hand landmarks if hands are detected
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # Get dimensions of the frame
                h, w, c = img.shape
                # Calculate coordinates of the landmark
                cx, cy = int(lm.x * w), int(lm.y * h)
                # Append landmark ID and coordinates to the list
                lmList.append([id, cx, cy])
                if draw:
                    # Draw circles on the landmarks
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        return lmList

# Main function to initialize video capture and hand detection
def main():
    # Variables to calculate frames per second (FPS)
    previousTime = currentTime = 0

    # Initialize video capture object to read from webcam
    capture = cv2.VideoCapture(0)

    # Initialize hand detector
    detector = HandDetector()

    while True:
        # Read frame from webcam
        success, vidObject = capture.read()

        if not success:
            break

        # Detect hands in the frame
        vidObject = detector.detectHands(vidObject)

        # Find positions of hand landmarks
        lmList = detector.findPosition(vidObject)
        
        if len(lmList) != 0:
            pass  # Perform any required operation with the landmarks

        # Calculate FPS
        currentTime = time.time()
        fps = 1 / (currentTime - previousTime)
        previousTime = currentTime

        # Display FPS on the frame
        cv2.putText(vidObject, f"FPS : {int(fps)}", (40, 70), cv2.FONT_ITALIC, 1, (0, 255, 0), 3)
        # Show the frame with hand landmarks
        cv2.imshow("Video", vidObject)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all OpenCV windows
    capture.release()
    cv2.destroyAllWindows()

# Entry point of the script
if __name__ == "__main__":
    main()
