# Import the needed modules
from time import sleep
import cv2
import numpy as np

# Start video capture from the camera with OpenCV
cv2.startWindowThread()
capture = cv2.VideoCapture(0)

# Set the HOG-SVM people detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Start the while loop to detect human from camera feeds
# It will run in infinite loop unless the user does the specified action in the last if block
whileLoopIterator = True
amt = 0

while(whileLoopIterator):
    ret,frame = capture.read() # reading the capture
    frame = cv2.resize(frame, (640, 480)) # resizing the capture
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # turning the capture into grayscale

    # detection start
    humans,_ =hog.detectMultiScale(frame, winStride=(12, 12), padding=(24, 24), scale=1.05)

    # count the current amount of human detected
    currentAmt = len(humans)

    # do something if amount of human detected change
    if currentAmt > amt:
        amt = currentAmt
        print("Amount increased to", amt)
    elif currentAmt < amt:
        amt = currentAmt
        print("Amount decreased to", amt)

    # if the current amount of human detected is zero, sleep for 10 seconds
    # then try to detect again, if still zero, turn off
    if currentAmt = 0:
        amt = currentAmt
        sleep(10)
        if currentAmt = 0:
            amt = currentAmt
            print("Turn off")
    # else, turn on
    elif currentAmt > 0:
        amt = currentAmt
        print("Turn on")

    # creating white block to detect human in the feed
    humans = np.array([[x, y, x + w, y + h] for (x, y, w, h) in humans])
    for (xA, yA, xB, yB) in humans:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB), (255, 255, 255), 2)

    cv2.imshow('frame',frame) # displaying the frame
    sleep(5) # bring the camera to sleep for 2 seconds for each loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # breaking the loop if the user types q
        # note that the video window must be highlighted!
        whileLoopIterator = False

capture.release()
cv2.destroyAllWindows()
